---
type: tool
title: Zod
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: library
problem: Validar datos en runtime con schemas que además generan los tipos de TypeScript — cierra el hueco de que los tipos desaparecen al compilar
alternatives: [Valibot, Yup, ajv]
integrates-with: ["[[typescript]]", "[[nextjs]]", "[[react]]"]
url: https://zod.dev
docs: https://zod.dev
tags: [topic/web, topic/backend]
aliases: []
---

# Zod

## Cuándo usarla

- En **toda frontera de datos externos**: request bodies, respuestas de APIs, formularios, variables de entorno. Lo que entra de fuera no es de fiar hasta que Zod lo valida.
- Como fuente única de verdad tipo+validación: `z.infer<typeof schema>` deriva el tipo del schema.

## Cuándo NO usarla

- Datos internos ya tipados: validar lo que TypeScript ya garantiza es ruido y coste.

## Ventajas

- Resuelve exactamente la desventaja documentada en [[typescript]]: "los tipos desaparecen en runtime".
- Composición de schemas elegante y mensajes de error estructurados.
- Estándar de facto: las librerías de formularios y frameworks lo integran nativamente.

## Desventajas

- Schemas muy grandes penalizan el type-checking del compilador.
- Duplicación conceptual si además existe un schema de BD (Prisma): tres fuentes de "forma de los datos" que mantener alineadas.

## Ejemplos de uso propios

- [[methodlife]]: validación en las fronteras del core.

## Notas de experiencia

- Promovida del Radar 2026-07-12: ya la usaba sin tenerla en el radar.
