---
type: tool
title: pnpm
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: cli
problem: Gestor de paquetes de Node más rápido y eficiente en disco que npm — un solo store global con enlaces, sin duplicar node_modules
alternatives: [npm, yarn, bun]
integrates-with: ["[[nodejs]]", "[[typescript]]"]
url: https://pnpm.io
docs: https://pnpm.io/motivation
tags: [topic/tooling]
aliases: []
---

# pnpm

## Cuándo usarla

- Cualquier proyecto Node nuevo: mismo `package.json`, instalaciones más rápidas y gigas de disco ahorrados.
- Monorepos: sus workspaces son de lo mejor del ecosistema.

## Cuándo NO usarla

- Proyectos de equipo ya estandarizados en npm/yarn: cambiar el gestor unilateralmente rompe lockfiles.

## Ventajas

- Store global con hard links: cada versión de cada paquete se guarda una sola vez en la máquina.
- `node_modules` estricto: solo se puede importar lo declarado (npm permite dependencias fantasma).

## Desventajas

- Algún paquete mal empaquetado asume la estructura laxa de npm y falla (raro en 2026).
- Un gestor más que recordar en máquinas nuevas (`corepack enable` lo alivia).

## Ejemplos de uso propios

- [[methodlife]] (MethodLife-game).

## Notas de experiencia

- Promovida del Radar 2026-07-12: ya la usaba sin tenerla en el radar.
