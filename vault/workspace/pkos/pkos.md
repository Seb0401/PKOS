---
type: project
title: PKOS — Personal Knowledge Operating System
created: 2026-07-07
updated: 2026-07-07
status: active
area: personal
started: 2026-07-07
finished:
stack: ["[[obsidian]]", "[[git]]", "[[markdown]]"]
repo:
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

## Tareas

- [ ] Configurar Obsidian sobre `vault/` y verificar plantillas
- [ ] Dar de alta el stack inicial en el Toolbox (fase 1)
- [ ] Registrar 3-5 decisiones reales más para validar la plantilla ADR

## Cronología

- 2026-07-07 — Fase 0: diseño del sistema, documentación (`docs/`), estructura del vault, plantillas y primeras decisiones.

## Ideas / Backlog

- `pkos lint`: validador de frontmatter y wikilinks (fase 5).
- Dashboard con Dataview cuando haya volumen real (fase 4).

## Enlaces

- Especificación: carpeta `docs/` del repositorio.
