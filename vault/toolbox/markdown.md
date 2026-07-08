---
type: tool
title: Markdown (CommonMark)
created: 2026-07-07
updated: 2026-07-07
status: adopted
category: other
problem: Formato de texto plano legible por humanos y parseable por máquinas para contenido estructurado que debe sobrevivir décadas a cualquier aplicación
alternatives: []
integrates-with: ["[[git]]", "[[obsidian]]"]
url: https://commonmark.org
docs: https://spec.commonmark.org
tags: [topic/pkm]
aliases: [Markdown]
---

# Markdown (CommonMark)

## Cuándo usarla

- Todo contenido de larga vida: documentación, notas, ADRs, READMEs.
- Cuando el contenido debe ser legible *sin ningún software* (un `.md` se lee en cualquier editor desde 1970 hasta 2070).

## Cuándo NO usarla

- Datos puramente tabulares o altamente estructurados sin prosa (mejor YAML/JSON/CSV — por eso el PKOS usa frontmatter YAML para los metadatos).
- Maquetación precisa (informes con diseño): ahí es un formato fuente que luego se transforma (Pandoc).

## Ventajas

- Diff-eable con [[git]]: el historial de un documento Markdown es legible línea a línea.
- CommonMark es una especificación formal: elimina las ambigüedades del Markdown original.
- Ecosistema universal: parsers maduros en todos los lenguajes (clave para la futura app del PKOS).

## Desventajas

- Los "sabores" (GFM, Obsidian, Pandoc) divergen en los extremos: tablas, footnotes, wikilinks. Mitigación en el PKOS: ceñirse a CommonMark + la única extensión decidida explícitamente ([[DEC-0002-wikilinks-y-nombres-unicos|DEC-0002]]).
- Sin validación de estructura por sí solo (por eso el contrato vive en el frontmatter, no en el cuerpo).

## Ejemplos de uso propios

- Todo el PKOS: `docs/` (spec) y `vault/` (conocimiento).

## Notas de experiencia

- La combinación frontmatter YAML + cuerpo CommonMark + wikilinks es el estándar de facto del ecosistema PKM (Obsidian, Logseq, Foam, Zettlr): apostar por ella maximiza compatibilidad futura.
