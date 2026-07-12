---
type: project
title: MethodLife — Gestión de vida con metodologías de ingeniería
created: 2026-07-12
updated: 2026-07-12
status: active
area: work
started: 2026-07-05
finished:
stack: ["[[typescript]]", "[[nextjs]]", "[[supabase]]", "[[postgresql]]", "[[tailwind]]", "[[react]]"]
repo: https://github.com/Seb0401/MethodLife
links: [https://github.com/Seb0401/MethodLife-game]
tags: [topic/web, topic/productividad, topic/ingenieria-de-software]
aliases: [MethodLife]
---

# MethodLife — Gestión de vida con metodologías de ingeniería

## Resumen

Aplicación de gestión de proyectos y vida personal que integra metodologías reales de ingeniería de software (Scrum, Kanban, FDD, XP, prototipado, métodos formales y trazabilidad) en un solo sistema. Organiza la vida en jerarquía: áreas → metas → proyectos → tareas.

Arquitectura en **dos repositorios sobre la misma BD de [[supabase]]**:

- **MethodLife** (core): Next.js 15 + App Router, TypeScript estricto, Prisma, RLS, logging inmutable por eventos, límites WIP.
- **MethodLife-game** (capa de gamificación): convierte la actividad real en XP, niveles y stats de un avatar. Solo *lee* los eventos del core y *escribe* únicamente en su tabla `xp_events`; nunca ejecuta migraciones. El estado del jugador es una función pura de los eventos.

## Objetivos

- Sistema multiusuario con autoridad del servidor sobre el estado y trazabilidad completa tarea → meta.
- Validar que la separación core/juego por permisos de BD se sostiene al crecer.

## Decisiones

<!-- la separación en dos repos con BD compartida y permisos asimétricos merece su propia DEC-NNNN -->

## Tareas

- [ ] Core: salir de fase de diseño hacia funcionalidad base
- [ ] Game: recompensas por sprint, atribución por feature, mecánicas avanzadas (buffs, boss fights)

## Cronología

- 2026-07-12 — Alta en el PKOS. Game ya tiene auth compartida, sync idempotente de XP y modo demo.
- 2026-07-11 — Inicio del repo MethodLife-game.
- 2026-07-05 — Inicio del repo core.

## Ideas / Backlog

- La relación con el PKOS es evidente: ambos gestionan proyectos/vida. Definir fronteras para no duplicar sistemas (¿MethodLife ejecuta, PKOS documenta?).

## Enlaces

- Repo core: https://github.com/Seb0401/MethodLife
- Repo game: https://github.com/Seb0401/MethodLife-game
