---
type: tool
title: PostgreSQL
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: database
problem: Base de datos relacional open source de referencia — integridad estricta, tipos ricos y extensibilidad para casi cualquier carga
alternatives: ["[[mysql]]", "[[mongodb]]"]
integrates-with: ["[[express]]", "[[docker]]"]
url: https://www.postgresql.org
docs: https://www.postgresql.org/docs/
tags: [topic/databases]
aliases: [Postgres]
---

# PostgreSQL

## Cuándo usarla

- Opción por defecto para cualquier proyecto nuevo que necesite una base de datos seria.
- Cuando los datos mezclan relacional + documentos: su tipo JSONB cubre gran parte de los casos de uso de [[mongodb]].

## Cuándo NO usarla

- Apps embebidas o locales de un solo usuario: SQLite es más simple (candidato para el índice derivado de la futura app del PKOS).
- Caching o datos efímeros: ahí Redis.

## Ventajas

- Rigurosa con el estándar SQL y la integridad: los errores explotan pronto, que es donde deben explotar.
- Extensible: PostGIS (geo), pgvector (embeddings/IA), full-text search integrado.
- Comunidad open source sin dueño corporativo único.

## Desventajas

- Administración algo más exigente que MySQL (tuning, vacuum) al crecer.
- Menos presente en hosting compartido barato.

## Ejemplos de uso propios

<!-- pendiente: añadir proyectos o ejercicios concretos donde la usé -->

## Notas de experiencia

- Nivel autodeclarado (2026-07-12): la he usado sin considerarme experto.
