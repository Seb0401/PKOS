---
type: tool
title: Vite
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: cli
problem: Servidor de desarrollo instantáneo y build de producción para frontend, sin la lentitud ni la configuración de los bundlers clásicos
alternatives: [webpack, esbuild, Parcel]
integrates-with: ["[[typescript]]", "[[javascript]]", "[[react]]", "[[nodejs]]"]
url: https://vite.dev
docs: https://vite.dev/guide/
tags: [topic/web, topic/tooling]
aliases: []
---

# Vite

## Cuándo usarla

- SPAs y proyectos frontend sin necesidades de servidor: arranque en milisegundos y config casi nula.
- Cuando [[nextjs]] sería exceso: simuladores, juegos, herramientas cliente puras (decisión de RPGSO).

## Cuándo NO usarla

- Si necesitas SSR/rutas de API integradas: eso es terreno de un framework completo como Next.

## Ventajas

- Dev server sobre ES modules nativos: recarga instantánea incluso en proyectos grandes.
- Config por defecto sensata: TypeScript, JSX y CSS funcionan sin tocar nada.
- Se ha vuelto la base de medio ecosistema (Astro, SvelteKit, Vitest la usan por debajo).

## Desventajas

- Dev (esbuild) y build (Rollup) usan pipelines distintos: raras veces, un bug aparece solo en producción.
- Para necesidades exóticas de bundling, el ecosistema de plugins es más joven que el de webpack.

## Ejemplos de uso propios

- [[rpgso]]: núcleo de simulación TypeScript + observatorio visual, sin framework de servidor.

## Notas de experiencia

<!-- pendiente: impresiones tras más uso real -->
