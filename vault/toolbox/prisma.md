---
type: tool
title: Prisma
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: library
problem: ORM tipado para Node/TypeScript — el schema de la BD genera tipos, cliente de consultas y migraciones desde una sola fuente
alternatives: [Drizzle, Kysely, SQL directo]
integrates-with: ["[[typescript]]", "[[postgresql]]", "[[mysql]]", "[[supabase]]", "[[nodejs]]"]
url: https://www.prisma.io
docs: https://www.prisma.io/docs
tags: [topic/databases, topic/backend]
aliases: []
---

# Prisma

## Cuándo usarla

- Backend TypeScript sobre BD relacional: el autocompletado tipado de consultas elimina una clase entera de bugs.
- Cuando quieres migraciones versionadas derivadas del schema (`schema.prisma` como fuente de verdad — filosofía familiar).

## Cuándo NO usarla

- Consultas SQL complejas (window functions, CTEs recursivas): el ORM estorba; mejor SQL directo o Kysely.
- Con [[supabase]] hay solapamiento: Supabase ya da un cliente — usar ambos exige decidir quién es dueño del schema.

## Ventajas

- Tipos generados: si la consulta compila, los campos existen.
- `prisma migrate` lleva el schema con la disciplina de Git.
- Soporta todas mis BDs ([[postgresql]], [[mysql]], [[mongodb]]).

## Desventajas

- Motor de consultas propio (histórico en Rust): capa opaca cuando algo va mal.
- Las consultas que genera no siempre son las óptimas; en hot paths hay que revisar el SQL real.

## Ejemplos de uso propios

- [[methodlife]]: ORM sobre la BD de Supabase, conviviendo con RLS.

## Notas de experiencia

- Promovida del Radar 2026-07-12. Pregunta abierta anotada: en MethodLife, ¿quién manda sobre el schema — Prisma o Supabase? Candidata a DEC del proyecto.
