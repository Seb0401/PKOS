---
type: decision
id: DEC-0001
title: Markdown plano + YAML como única fuente de verdad
created: 2026-07-07
updated: 2026-07-07
status: accepted
date: 2026-07-07
scope: architecture
context-of: "[[pkos]]"
supersedes:
superseded-by:
tags: [topic/pkos]
aliases: [DEC-0001]
---

# DEC-0001 — Markdown plano + YAML como única fuente de verdad

## Contexto

El PKOS debe durar toda una carrera profesional (30-40 años) y sobrevivir a cualquier aplicación concreta. Se necesita un formato de almacenamiento para conocimiento estructurado (proyectos, planes, herramientas, decisiones) que hoy consumirá Obsidian y mañana una aplicación propia.

## Alternativas consideradas

### Opción A — Base de datos de una app (Notion, Anytype, SQLite propia)

- ✅ Consultas potentes desde el día uno; relaciones y vistas nativas.
- ❌ El conocimiento queda rehén del proveedor o de un código que aún no existe; exportar es siempre con pérdida.
- ❌ No versionable con Git de forma legible (diffs binarios u opacos).

### Opción B — Markdown puro sin metadatos estructurados

- ✅ Máxima simplicidad y portabilidad.
- ❌ Inconsultable: "todos los proyectos activos" exigiría parsear prosa. Sin discriminador de tipos, la app futura no tiene contrato.

### Opción C — Markdown (CommonMark) + frontmatter YAML *(elegida)*

- ✅ Legible sin software, versionable con Git, editable con cualquier editor durante décadas.
- ✅ El frontmatter da la parte "base de datos" (campos tipados, enums, relaciones) manteniendo texto plano.
- ✅ Estándar de facto: Obsidian, Hugo, Jekyll, Zettlr, Logseq y decenas de parsers en todos los lenguajes lo entienden hoy.
- ❌ Las consultas requieren tooling (Dataview ahora, parser propio después): coste asumido y planificado (fases 4-5 del roadmap).
- ❌ Sin validación nativa: un typo en `status` no da error. Mitigado con plantillas ahora y `pkos lint` en fase 5.

## Decisión

Todo el conocimiento vive en archivos Markdown con frontmatter YAML dentro de `vault/`, según los schemas de `docs/02-data-model.md`. Ninguna información original puede existir solo en un plugin, una app o una base de datos externa; cualquier índice o vista debe ser derivable de los archivos.

## Consecuencias esperadas

- Se gana longevidad y libertad total de aplicación; se sacrifica potencia de consulta a corto plazo.
- Obliga a disciplina de frontmatter: el valor del sistema es proporcional a la consistencia de los metadatos.
- La app futura empieza con un parser de este formato, no con un diseño de BD desde cero.

## Lecciones aprendidas

- (pendiente de revisión — programada para ~2027-01)
