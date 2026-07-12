---
type: tool
title: Vitest
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: testing
problem: Test runner para JavaScript/TypeScript nativo del ecosistema Vite — rápido, con ESM y TypeScript sin configuración
alternatives: [Jest]
integrates-with: ["[[vite]]", "[[typescript]]", "[[react]]"]
url: https://vitest.dev
docs: https://vitest.dev/guide/
tags: [topic/testing]
aliases: []
---

# Vitest

## Cuándo usarla

- Tests unitarios y de lógica de dominio en cualquier proyecto TypeScript moderno (es el default de 2026: 3-5x más rápido que Jest).
- Proyectos que ya usan [[vite]]: comparte config y pipeline.

## Cuándo NO usarla

- Tests end-to-end de navegador real: eso es terreno de [[playwright]].
- Proyectos legacy anclados a Jest donde migrar no paga.

## Ventajas

- TypeScript y ESM funcionan sin plugins ni transformadores.
- API compatible con Jest: migrar es mayormente cambiar el import.
- Watch mode inteligente: solo re-ejecuta los tests afectados por el cambio.

## Desventajas

- Ecosistema de snapshots/mocks algo más joven que el de Jest en casos exóticos.

## Ejemplos de uso propios

- [[methodlife]]: tests de la lógica de dominio (funciones puras de XP en MethodLife-game).

## Notas de experiencia

- Promovida del Radar 2026-07-12: ya la usaba sin tenerla en el radar. Primera herramienta de la categoría `testing`.
