#!/usr/bin/env python3
"""pkos stats — dashboard HTML derivado del vault.

Parsea el frontmatter de todas las notas de `vault/` (según el contrato de
`docs/02-data-model.md`) y genera un HTML autocontenido con estadísticas:
tech radar del Toolbox, WIP del Workspace, progreso del Learning Hub,
estado del Decision Journal y salud del vault (mini-lint).

La salida es una VISTA DERIVADA: se puede borrar y regenerar siempre
(regla de docs/01-architecture.md). Este parser es el embrión de
`pkos lint` (fase 5) y de la app propia (fase 6). Ver DEC-0007.

Uso:
    python tools/pkos_stats.py [--vault vault] [--out tools/out/stats.html]

Sin dependencias obligatorias: usa PyYAML si está instalado y, si no,
un parser propio del subconjunto de YAML que permite el contrato.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import math
import re
from pathlib import Path

try:
    import yaml  # type: ignore

    HAVE_YAML = True
except ImportError:
    HAVE_YAML = False

# ── Contrato de datos (espejo de docs/02-data-model.md) ─────────────────────

REQUIRED_FIELDS = ["type", "title", "created", "updated", "status"]

STATUS_ENUM = {
    "project": ["idea", "active", "paused", "done", "archived"],
    "learning-plan": ["planned", "in-progress", "done", "abandoned"],
    "tool": ["evaluating", "adopted", "deprecated", "discarded"],
    "decision": ["proposed", "accepted", "superseded", "deprecated"],
}

CATEGORY_ENUM = [
    "language", "framework", "database", "devops", "testing", "ai",
    "service", "cli", "library", "runtime", "app", "format", "other",
]

AREA_ENUM = ["work", "personal", "oss", "freelance"]
SCOPE_ENUM = ["architecture", "tooling", "process", "career", "learning"]

# Tipos fuera del contrato tolerados en dashboards/índices (no se lintean).
VIEW_TYPES = {"dashboard"}

STALE_DAYS = 60  # una nota sin `updated` en 60 días se considera fría

# ── Paleta (coherente con vault/.obsidian/snippets/pkos-colors.css) ─────────

C = {
    "workspace": "#3b82f6",
    "learning": "#22c55e",
    "toolbox": "#f59e0b",
    "decisions": "#a855f7",
    "inbox": "#ef4444",
    "accent": "#8b5cf6",
    "bg": "#0f0f14",
    "card": "#17171f",
    "border": "#2a2a38",
    "text": "#e5e5ee",
    "muted": "#9a9ab0",
}

RADAR_QUADRANTS = [
    ("Lenguajes y formatos", ["language", "format"], "#3b82f6"),
    ("Web y datos", ["framework", "library", "runtime", "database", "service"], "#f59e0b"),
    ("DevOps y tooling", ["devops", "cli", "testing"], "#22c55e"),
    ("IA y apps", ["ai", "app", "other"], "#a855f7"),
]

RADAR_RINGS = ["adopted", "evaluating", "deprecated", "discarded"]

# El target termina en `|` (alias), `#` (heading) o `\` (pipe escapado en tablas).
WIKILINK_RE = re.compile(r"\[\[([^\]|#\\]+)(?:\\?\|[^\]]*)?(?:#[^\]]*)?\]\]")
CHECKBOX_RE = re.compile(r"^\s*-\s\[([ xX])\]", re.MULTILINE)
# Código inline y bloques de código: ahí los wikilinks son ejemplos, no enlaces.
CODE_RE = re.compile(r"```.*?```|`[^`\n]*`", re.DOTALL)


# ── Parseo ───────────────────────────────────────────────────────────────────

def parse_scalar(raw: str):
    v = raw.strip()
    if v == "":
        return None
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def parse_frontmatter_fallback(block: str) -> dict:
    """Subconjunto de YAML del contrato: `clave: valor` y listas inline."""
    data: dict = {}
    for line in block.splitlines():
        if not line or line.startswith("#") or line.startswith(" "):
            continue
        if ":" not in line:
            continue
        key, _, raw = line.partition(":")
        raw = raw.strip()
        if raw.startswith("[") and raw.endswith("]"):
            inner = raw[1:-1].strip()
            data[key.strip()] = (
                [parse_scalar(x) for x in inner.split(",")] if inner else []
            )
        else:
            data[key.strip()] = parse_scalar(raw)
    return data


def parse_note(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8-sig")
    if not text.startswith("---"):
        return {"fm": {}, "body": text}
    end = text.find("\n---", 3)
    if end == -1:
        return {"fm": {}, "body": text}
    block = text[4:end]
    body = text[end + 4:]
    if HAVE_YAML:
        try:
            fm = yaml.safe_load(block) or {}
        except yaml.YAMLError:
            fm = parse_frontmatter_fallback(block)
    else:
        fm = parse_frontmatter_fallback(block)
    if not isinstance(fm, dict):
        fm = {}
    return {"fm": fm, "body": body}


def load_vault(vault: Path) -> list[dict]:
    notes = []
    for path in sorted(vault.rglob("*.md")):
        rel = path.relative_to(vault)
        parts = rel.parts
        if parts[0] == ".obsidian":
            continue
        parsed = parse_note(path)
        module = parts[0] if len(parts) > 1 else "(raíz)"
        notes.append({
            "slug": path.stem,
            "rel": str(rel).replace("\\", "/"),
            "module": module,
            "special": parts[0].startswith("_"),
            "fm": parsed["fm"],
            "body": parsed["body"],
            "raw_links": WIKILINK_RE.findall(
                CODE_RE.sub(" ", parsed["body"]) + " " + str(parsed["fm"])
            ),
        })
    return notes


# ── Análisis ─────────────────────────────────────────────────────────────────

def as_date(value) -> dt.date | None:
    if isinstance(value, dt.date):
        return value
    if isinstance(value, str):
        try:
            return dt.date.fromisoformat(value.strip())
        except ValueError:
            return None
    return None


def lint(notes: list[dict], slugs: set[str]) -> dict:
    issues: list[str] = []
    broken: list[tuple[str, str]] = []
    incoming: dict[str, int] = {s: 0 for s in slugs}

    for n in notes:
        for target in n["raw_links"]:
            target = target.strip()
            if target in slugs:
                if target != n["slug"]:
                    incoming[target] += 1
            elif not n["special"] and n["module"] != "_templates":
                broken.append((n["rel"], target))

        if n["special"]:
            continue
        fm, t = n["fm"], n["fm"].get("type")
        if t in VIEW_TYPES:
            continue
        if t not in STATUS_ENUM:
            issues.append(f"{n['rel']} — type desconocido: {t!r}")
            continue
        for field in REQUIRED_FIELDS:
            if fm.get(field) in (None, ""):
                issues.append(f"{n['rel']} — falta el campo obligatorio `{field}`")
        status = fm.get("status")
        if status and status not in STATUS_ENUM[t]:
            issues.append(f"{n['rel']} — status inválido para {t}: {status!r}")
        if t == "tool":
            cat = fm.get("category")
            if cat and cat not in CATEGORY_ENUM:
                issues.append(f"{n['rel']} — category inválida: {cat!r}")
            if not fm.get("problem"):
                issues.append(f"{n['rel']} — falta `problem` (obligatorio en tool)")
        if t == "project" and fm.get("area") not in AREA_ENUM:
            issues.append(f"{n['rel']} — area inválida: {fm.get('area')!r}")
        if t == "decision" and fm.get("scope") not in SCOPE_ENUM:
            issues.append(f"{n['rel']} — scope inválido: {fm.get('scope')!r}")

    orphans = [
        n["rel"] for n in notes
        if not n["special"]
        and n["fm"].get("type") not in VIEW_TYPES
        and incoming.get(n["slug"], 0) == 0
    ]

    today = dt.date.today()
    stale = []
    for n in notes:
        if n["special"] or n["fm"].get("type") in VIEW_TYPES:
            continue
        upd = as_date(n["fm"].get("updated"))
        if upd and (today - upd).days > STALE_DAYS:
            stale.append((n["rel"], (today - upd).days))
    return {"issues": issues, "broken": broken, "orphans": orphans, "stale": stale}


def checkbox_progress(body: str) -> tuple[int, int]:
    marks = CHECKBOX_RE.findall(body)
    done = sum(1 for m in marks if m in "xX")
    return done, len(marks)


# ── Helpers SVG / HTML ───────────────────────────────────────────────────────

def esc(s) -> str:
    return html.escape(str(s), quote=True)


def status_chip(status: str) -> str:
    colors = {
        "active": C["learning"], "in-progress": C["learning"],
        "adopted": C["learning"], "accepted": C["learning"],
        "evaluating": C["toolbox"], "proposed": C["toolbox"],
        "planned": C["toolbox"], "idea": C["toolbox"],
        "paused": C["muted"], "done": C["workspace"],
        "archived": C["muted"], "deprecated": C["inbox"],
        "discarded": C["inbox"], "superseded": C["muted"],
        "abandoned": C["inbox"],
    }
    col = colors.get(status, C["muted"])
    return (
        f'<span class="chip" style="border-color:{col};color:{col}">'
        f"{esc(status)}</span>"
    )


def bar_row(label: str, count: int, total: int, color: str) -> str:
    pct = 0 if total == 0 else round(100 * count / total)
    return (
        f'<div class="bar-row"><span class="bar-label">{esc(label)}</span>'
        f'<div class="bar-track"><div class="bar-fill" '
        f'style="width:{pct}%;background:{color}"></div></div>'
        f'<span class="bar-count">{count}</span></div>'
    )


def radar_svg(tools: list[dict]) -> str:
    """Tech radar: anillos = status, cuadrantes = grupos de categorías."""
    size, cx, cy = 720, 360, 360
    bands = [(0, 100), (100, 175), (175, 240), (240, 295)]
    parts = [
        f'<svg viewBox="0 0 {size} {size}" class="radar" '
        f'xmlns="http://www.w3.org/2000/svg" role="img">'
    ]
    for _, outer in reversed(bands):
        parts.append(
            f'<circle cx="{cx}" cy="{cy}" r="{outer}" fill="none" '
            f'stroke="{C["border"]}" stroke-width="1"/>'
        )
    parts.append(
        f'<line x1="{cx}" y1="{cy - 295}" x2="{cx}" y2="{cy + 295}" '
        f'stroke="{C["border"]}"/>'
        f'<line x1="{cx - 295}" y1="{cy}" x2="{cx + 295}" y2="{cy}" '
        f'stroke="{C["border"]}"/>'
    )
    ring_label_y = [55, 140, 208, 268]
    for ring, y in zip(RADAR_RINGS, ring_label_y):
        parts.append(
            f'<text x="{cx}" y="{cy - y}" text-anchor="middle" '
            f'class="ring-label">{ring}</text>'
        )
    corner = [(14, 26), (size - 14, 26), (14, size - 12), (size - 14, size - 12)]
    anchors = ["start", "end", "start", "end"]
    quad_angles = [(180, 270), (270, 360), (90, 180), (0, 90)]

    for qi, (qname, qcats, qcolor) in enumerate(RADAR_QUADRANTS):
        x, y = corner[qi]
        parts.append(
            f'<text x="{x}" y="{y}" text-anchor="{anchors[qi]}" '
            f'class="quad-label" fill="{qcolor}">{esc(qname)}</text>'
        )
        a0, a1 = quad_angles[qi]
        for ri, ring in enumerate(RADAR_RINGS):
            items = [
                t for t in tools
                if t["fm"].get("category", "other") in qcats
                and t["fm"].get("status") == ring
            ]
            r0, r1 = bands[ri]
            for i, t in enumerate(items):
                frac = (i + 1) / (len(items) + 1)
                ang = math.radians(a0 + 12 + frac * (a1 - a0 - 24))
                rad = r0 + (0.35 + 0.3 * (i % 2)) * (r1 - r0)
                px = cx + rad * math.cos(ang)
                py = cy + rad * math.sin(ang)
                name = t["fm"].get("title", t["slug"])
                parts.append(
                    f'<g class="dot"><circle cx="{px:.1f}" cy="{py:.1f}" r="6" '
                    f'fill="{qcolor}" fill-opacity="0.9"/>'
                    f'<text x="{px + 9:.1f}" y="{py + 3:.1f}" class="dot-label">'
                    f"{esc(t['slug'])}</text>"
                    f"<title>{esc(name)} — {esc(ring)}</title></g>"
                )
    parts.append("</svg>")
    return "".join(parts)


# ── Render del dashboard ─────────────────────────────────────────────────────

def build_html(notes: list[dict], lint_result: dict) -> str:
    today = dt.date.today().isoformat()
    entities = [n for n in notes if not n["special"]]
    by_type: dict[str, list[dict]] = {}
    for n in entities:
        by_type.setdefault(str(n["fm"].get("type")), []).append(n)

    tools = by_type.get("tool", [])
    projects = by_type.get("project", [])
    plans = by_type.get("learning-plan", [])
    decisions = sorted(
        by_type.get("decision", []), key=lambda n: str(n["fm"].get("id"))
    )
    inbox = [n for n in notes if n["module"] == "_inbox"]

    # — Header: totales —
    totals = [
        ("notas", len(notes)), ("herramientas", len(tools)),
        ("proyectos", len(projects)), ("decisiones", len(decisions)),
        ("planes", len(plans)), ("digests sin triar", len(inbox)),
    ]
    totals_html = "".join(
        f'<div class="stat"><div class="stat-n">{v}</div>'
        f'<div class="stat-l">{esc(k)}</div></div>' for k, v in totals
    )

    # — Salud —
    li = lint_result
    ok = not (li["issues"] or li["broken"])
    health_items = []
    if li["broken"]:
        health_items += [
            f"🔗 wikilink roto <code>[[{esc(t)}]]</code> en {esc(f)}"
            for f, t in li["broken"]
        ]
    health_items += ["⚠️ " + esc(i) for i in li["issues"]]
    health_items += [f"👻 sin enlaces entrantes: {esc(o)}" for o in li["orphans"]]
    health_items += [
        f"🧊 {esc(f)} lleva {d} días sin actualizar" for f, d in li["stale"]
    ]
    health_html = (
        '<p class="ok">✅ Contrato de datos íntegro: sin wikilinks rotos ni '
        "frontmatter inválido.</p>" if ok else ""
    ) + (
        "<ul>" + "".join(f"<li>{x}</li>" for x in health_items) + "</ul>"
        if health_items else ""
    )

    # — Toolbox —
    status_count = {s: 0 for s in RADAR_RINGS}
    for t in tools:
        s = t["fm"].get("status")
        if s in status_count:
            status_count[s] += 1
    tool_bars = "".join(
        bar_row(s, c, len(tools), C["toolbox"]) for s, c in status_count.items()
    )
    tool_rows = "".join(
        f"<tr><td>{esc(t['fm'].get('title', t['slug']))}</td>"
        f"<td>{esc(t['fm'].get('category', ''))}</td>"
        f"<td>{status_chip(str(t['fm'].get('status')))}</td>"
        f"<td class='muted'>{esc(t['fm'].get('problem', ''))}</td></tr>"
        for t in sorted(tools, key=lambda x: (
            str(x["fm"].get("category")), x["slug"]))
    )

    # — Workspace —
    active = [p for p in projects if p["fm"].get("status") == "active"]
    wip_warn = (
        f'<p class="warn">⚠️ {len(active)} proyectos <b>active</b> a la vez — '
        "revisa si alguno es honesto pasarlo a <code>paused</code>.</p>"
        if len(active) > 4 else ""
    )
    area_count: dict[str, int] = {}
    for p in projects:
        area_count[str(p["fm"].get("area"))] = (
            area_count.get(str(p["fm"].get("area")), 0) + 1
        )
    project_bars = "".join(
        bar_row(a, c, len(projects), C["workspace"])
        for a, c in sorted(area_count.items())
    )
    project_cards = "".join(
        f'<div class="card mini"><b>{esc(p["fm"].get("title", p["slug"]))}</b> '
        f"{status_chip(str(p['fm'].get('status')))}"
        f'<div class="muted">{esc(p["fm"].get("area", ""))}'
        f' · desde {esc(p["fm"].get("started", "?"))}</div></div>'
        for p in projects
    )

    # — Learning —
    plan_bars = []
    for p in plans:
        done, total = checkbox_progress(p["body"])
        pct = 0 if total == 0 else round(100 * done / total)
        plan_bars.append(
            f'<div class="plan"><b>{esc(p["fm"].get("title", p["slug"]))}</b> '
            f"{status_chip(str(p['fm'].get('status')))}"
            f'<div class="bar-track big"><div class="bar-fill" '
            f'style="width:{pct}%;background:{C["learning"]}"></div></div>'
            f'<span class="muted">{done}/{total} pasos · {pct}%</span>'
            f'<div class="muted">🎯 {esc(p["fm"].get("goal", ""))}</div></div>'
        )
    learning_html = "".join(plan_bars) or '<p class="muted">Sin planes aún.</p>'

    # — Decisiones —
    pending = [
        d for d in decisions
        if "pendiente" in d["body"].split("Lecciones aprendidas")[-1][:200].lower()
    ]
    dec_rows = "".join(
        f"<tr><td><b>{esc(d['fm'].get('id'))}</b></td>"
        f"<td>{esc(d['fm'].get('title'))}</td>"
        f"<td>{esc(d['fm'].get('scope'))}</td>"
        f"<td>{status_chip(str(d['fm'].get('status')))}</td>"
        f"<td class='muted'>{esc(d['fm'].get('date'))}</td></tr>"
        for d in decisions
    )

    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PKOS · stats</title>
<style>
  :root {{ color-scheme: dark; }}
  * {{ box-sizing: border-box; margin: 0; }}
  body {{ background:{C['bg']}; color:{C['text']};
    font: 15px/1.55 system-ui, 'Segoe UI', sans-serif; padding: 24px; }}
  h1 {{ font-size: 1.6em; }} h2 {{ font-size: 1.15em; margin-bottom: 12px; }}
  header {{ display:flex; flex-wrap:wrap; align-items:baseline; gap:12px;
    margin-bottom:20px; }}
  .muted {{ color:{C['muted']}; font-size:.92em; }}
  nav a {{ color:{C['accent']}; text-decoration:none; margin-right:14px; }}
  .grid {{ display:grid; gap:16px;
    grid-template-columns:repeat(auto-fit,minmax(340px,1fr)); }}
  .card {{ background:{C['card']}; border:1px solid {C['border']};
    border-radius:12px; padding:18px; margin-bottom:16px; }}
  .card.mini {{ margin:0; }}
  .stats {{ display:flex; flex-wrap:wrap; gap:22px; }}
  .stat-n {{ font-size:1.9em; font-weight:700; color:{C['accent']}; }}
  .stat-l {{ color:{C['muted']}; font-size:.85em; }}
  .chip {{ border:1px solid; border-radius:10px; padding:0 8px;
    font-size:.78em; white-space:nowrap; }}
  .bar-row {{ display:flex; align-items:center; gap:10px; margin:6px 0; }}
  .bar-label {{ width:110px; font-size:.88em; color:{C['muted']}; }}
  .bar-track {{ flex:1; height:10px; background:{C['bg']};
    border-radius:6px; overflow:hidden; }}
  .bar-track.big {{ height:14px; margin:8px 0 4px; }}
  .bar-fill {{ height:100%; border-radius:6px; }}
  .bar-count {{ width:28px; text-align:right; font-size:.88em; }}
  table {{ width:100%; border-collapse:collapse; font-size:.92em; }}
  th, td {{ text-align:left; padding:7px 10px;
    border-bottom:1px solid {C['border']}; vertical-align:top; }}
  th {{ color:{C['muted']}; font-weight:600; }}
  input#q {{ background:{C['bg']}; border:1px solid {C['border']};
    color:{C['text']}; border-radius:8px; padding:8px 12px; width:100%;
    margin-bottom:10px; }}
  .radar {{ max-width:720px; width:100%; display:block; margin:0 auto; }}
  .ring-label {{ fill:{C['muted']}; font-size:11px; text-anchor:middle;
    text-transform:uppercase; letter-spacing:.08em; }}
  .quad-label {{ font-size:13px; font-weight:700; }}
  .dot-label {{ fill:{C['text']}; font-size:9.5px; opacity:.75; }}
  .dot:hover circle {{ r:8; }} .dot:hover .dot-label {{ opacity:1;
    font-weight:700; }}
  .ok {{ color:{C['learning']}; }} .warn {{ color:{C['toolbox']}; }}
  ul {{ padding-left:20px; }} li {{ margin:3px 0; }}
  code {{ background:{C['bg']}; padding:1px 5px; border-radius:5px; }}
  .plan {{ margin-bottom:16px; }}
  footer {{ margin-top:24px; color:{C['muted']}; font-size:.85em; }}
</style></head><body>
<header>
  <h1>🧠 PKOS · stats</h1>
  <span class="muted">vista derivada · generada {today}</span>
  <nav><a href="#salud">salud</a><a href="#radar">radar</a>
  <a href="#proyectos">proyectos</a><a href="#learning">learning</a>
  <a href="#decisiones">decisiones</a></nav>
</header>

<div class="card"><div class="stats">{totals_html}</div></div>

<div class="card" id="salud"><h2>🩺 Salud del vault</h2>{health_html}</div>

<div class="card" id="radar">
  <h2>🧰 Tech radar — {len(tools)} herramientas</h2>
  {radar_svg(tools)}
  <div style="max-width:520px;margin:14px auto 0">{tool_bars}</div>
</div>

<div class="card">
  <h2>🔎 Toolbox en detalle</h2>
  <input id="q" placeholder="filtrar herramientas… (nombre, categoría, estado)">
  <table id="tools"><thead><tr><th>Herramienta</th><th>Categoría</th>
  <th>Estado</th><th>Problema que resuelve</th></tr></thead>
  <tbody>{tool_rows}</tbody></table>
</div>

<div class="card" id="proyectos">
  <h2>🗂️ Workspace — {len(projects)} proyectos</h2>
  {wip_warn}
  <div class="grid">{project_cards}</div>
  <div style="max-width:520px;margin-top:14px">{project_bars}</div>
</div>

<div class="card" id="learning">
  <h2>📚 Learning Hub — {len(plans)} plan(es)</h2>{learning_html}
</div>

<div class="card" id="decisiones">
  <h2>⚖️ Decision Journal — {len(decisions)} decisiones
  <span class="muted">({len(pending)} con lecciones pendientes)</span></h2>
  <table><thead><tr><th>ID</th><th>Decisión</th><th>Ámbito</th>
  <th>Estado</th><th>Fecha</th></tr></thead><tbody>{dec_rows}</tbody></table>
</div>

<footer>Generado por <code>tools/pkos_stats.py</code> · los datos viven en
<code>vault/</code>, esta página es desechable (DEC-0007).</footer>

<script>
  const q = document.getElementById('q');
  q.addEventListener('input', () => {{
    const term = q.value.toLowerCase();
    for (const tr of document.querySelectorAll('#tools tbody tr'))
      tr.style.display =
        tr.textContent.toLowerCase().includes(term) ? '' : 'none';
  }});
</script>
</body></html>"""


def main() -> int:
    ap = argparse.ArgumentParser(description="Genera el dashboard de stats del PKOS")
    ap.add_argument("--vault", default="vault", help="ruta al vault (default: vault)")
    ap.add_argument("--out", default="tools/out/stats.html", help="HTML de salida")
    args = ap.parse_args()

    vault = Path(args.vault)
    if not vault.is_dir():
        print(f"error: no existe el vault en {vault.resolve()}")
        return 1

    notes = load_vault(vault)
    slugs = {n["slug"] for n in notes}
    result = lint(notes, slugs)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_html(notes, result), encoding="utf-8")

    # Solo ASCII en consola: la de Windows suele ser cp1252 y explota con emoji.
    n_issues = len(result["issues"]) + len(result["broken"])
    print(f"[ok] {len(notes)} notas analizadas - {n_issues} problemas de contrato")
    print(f"[ok] dashboard: {out.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
