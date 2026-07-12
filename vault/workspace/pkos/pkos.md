---
type: project
title: PKOS — Personal Knowledge Operating System
created: 2026-07-07
updated: 2026-07-12
status: active
area: personal
started: 2026-07-07
finished:
stack: ["[[obsidian]]", "[[git]]", "[[markdown]]", "[[vscode]]", "[[claude-ai]]"]
repo: https://github.com/Seb0401/PKOS
links: []
tags: [topic/pkos]
aliases: [PKOS]
---

# PKOS — Personal Knowledge Operating System

## Resumen

Sistema personal de gestión de conocimiento en Markdown plano, independiente de aplicación. Este mismo vault es su producto: el proyecto se documenta a sí mismo (dogfooding).

## Objetivos

- Base de conocimiento portable que sobreviva a Obsidian y a cualquier app concreta.
- Cuatro módulos operativos: Workspace, Learning Hub, Toolbox, Decision Journal.
- A largo plazo: aplicación propia que consuma el mismo vault (fase 6 del roadmap).

## Decisiones

- [[DEC-0001-markdown-como-fuente-de-verdad|DEC-0001]] — Markdown + YAML como fuente de verdad.
- [[DEC-0002-wikilinks-y-nombres-unicos|DEC-0002]] — Wikilinks con nombres únicos.
- [[DEC-0003-autoria-unica-de-commits|DEC-0003]] — Autoría única de commits (proceso).
- [[DEC-0004-main-inmutable-tras-bootstrap|DEC-0004]] — Main inmutable tras el bootstrap (proceso).

## Tareas

- [x] Configurar Obsidian sobre `vault/` y verificar plantillas
- [x] Dar de alta el stack inicial en el Toolbox (fase 1)
- [x] Registrar 3-5 decisiones reales más para validar la plantilla ADR (DEC-0003, DEC-0004, DEC-0005)
- [ ] Completar "Ejemplos de uso propios" y "Notas de experiencia" de las tools del stack
- [ ] Rellenar "Lecciones aprendidas" de DEC-0001 a DEC-0005 (revisión ~2026-10)

## Cronología

- 2026-07-12 — **Primer código del sistema** ([[DEC-0007-primer-codigo-pkos-stats|DEC-0007]]): `tools/pkos_stats.py` genera un dashboard HTML derivado (tech radar visual, WIP, progreso de planes, mini-lint). El lint cazó su primer defecto real en DEC-0002 y aprendió 2 reglas de parseo (código inline, pipes escapados).
- 2026-07-12 — Primer triage del Radar: promovidas las 5 tools ya en uso (testing deja de ser categoría vacía). Fase 3 arrancada: [[plan-docker]] como primer learning-plan, con meta concreta ([[n8n]] self-hosted para la fase B del Radar).
- 2026-07-12 — [[DEC-0006-radar-de-descubrimiento|DEC-0006]] aceptada y primera corrida manual del Radar: digest en `_inbox/`, carpeta registrada en las convenciones. Hallazgo meta: 5 herramientas que ya uso (Vitest, Playwright, Prisma, Zod, pnpm) no estaban en el Toolbox — el radar sirve también hacia adentro.
- 2026-07-12 — Fase 2: alta de los 5 proyectos activos ([[methodlife]], [[tracereq]], [[vibelearning]], [[codventure]], [[rpgso]]) y de 5 tools de su stack ([[nextjs]], [[supabase]], [[tailwind]], [[flask]], [[vite]]). Fricción observada (1ª vez): el enum `area` no tiene valor claro para proyectos universitarios — se usó `work`; si vuelve a doler, candidato a DEC.
- 2026-07-12 — Primer cambio real del contrato de datos: [[DEC-0005-ampliar-enum-category|DEC-0005]] amplía el enum `category` (`runtime`, `app`, `format`) tras la segunda fricción — la regla de "doler dos veces" funcionó. Alta del stack real completo en el Toolbox (16 herramientas).
- 2026-07-12 — Obsidian verificado sobre el vault (plantillas con `{{date}}` funcionando). Fase 0 cerrada; comienza el grueso de la Fase 1: poblar el Toolbox con el stack real.
- 2026-07-07 — Gobernanza del historial de git: reescritura de `main` para eliminar coautoría y compactar el bootstrap (18 → 7 commits), registrada como [[DEC-0003-autoria-unica-de-commits|DEC-0003]] y [[DEC-0004-main-inmutable-tras-bootstrap|DEC-0004]]. La ventana de reescritura queda cerrada.
- 2026-07-07 — Config compartida de Obsidian versionada; plantillas con `{{date}}`; primeras tools en el Toolbox ([[git]], [[obsidian]], [[markdown]]). Fricción detectada: el enum `category` no encaja bien para apps/formatos (obsidian y markdown caen en `other`) — candidato a ajuste de schema si vuelve a doler.
- 2026-07-07 — Fase 0: diseño del sistema, documentación (`docs/`), estructura del vault, plantillas y primeras decisiones.

## Ideas / Backlog

- Radar ([[DEC-0006-radar-de-descubrimiento|DEC-0006]]): tras 3-4 corridas manuales, automatizar la recolección con [[n8n]] en [[docker]] (fase B).
- `pkos lint`: validador de frontmatter y wikilinks (fase 5).
- Dashboard con Dataview cuando haya volumen real (fase 4).

## Enlaces

- Especificación: carpeta `docs/` del repositorio.
