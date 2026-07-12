---
type: dashboard
title: Decision Journal
created: 2026-07-07
updated: 2026-07-12
---

# ⚖️ Decision Journal

Una decisión = un archivo `decisions/DEC-NNNN-<slug>.md` (schema `decision`, formato ADR extendido). ID secuencial global e inmutable. Plantilla: `_templates/decision.md`.

**Método**: registrar la decisión cuando se toma; volver a los 3-6 meses a rellenar "Lecciones aprendidas".

Ciclo de vida: `proposed → accepted → superseded / deprecated`. Ámbitos: `architecture` (el sistema), `tooling`, `process` (cómo se trabaja), `career`, `learning`.

## Revisiones programadas

- [ ] ~2026-10 — Lecciones aprendidas de DEC-0001 a DEC-0006

## Registro

| ID | Decisión | Estado | Ámbito | Fecha |
|---|---|---|---|---|
| [[DEC-0001-markdown-como-fuente-de-verdad\|DEC-0001]] | Markdown plano como fuente de verdad | accepted | architecture | 2026-07-07 |
| [[DEC-0002-wikilinks-y-nombres-unicos\|DEC-0002]] | Wikilinks con nombres de archivo únicos | accepted | architecture | 2026-07-07 |
| [[DEC-0003-autoria-unica-de-commits\|DEC-0003]] | Autoría única de commits: la IA prepara, el humano commitea | accepted | process | 2026-07-07 |
| [[DEC-0004-main-inmutable-tras-bootstrap\|DEC-0004]] | Historial de main inmutable tras el bootstrap | accepted | process | 2026-07-07 |
| [[DEC-0005-ampliar-enum-category\|DEC-0005]] | Ampliar el enum category con runtime, app y format | accepted | architecture | 2026-07-12 |
| [[DEC-0006-radar-de-descubrimiento\|DEC-0006]] | Radar de descubrimiento: pipeline de entrada al Toolbox | accepted | process | 2026-07-12 |

**Próximo ID libre: DEC-0007**
