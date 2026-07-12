---
type: decision
id: DEC-0007
title: Primer código del sistema — pkos stats como embrión del parser
created: 2026-07-12
updated: 2026-07-12
status: accepted
date: 2026-07-12
scope: architecture
context-of: "[[pkos]]"
supersedes:
superseded-by:
tags: [topic/pkos]
aliases: [DEC-0007]
---

# DEC-0007 — Primer código del sistema: `pkos stats` como embrión del parser

## Contexto

Se quería un dashboard más visual e interactivo con estadísticas del sistema. El roadmap contemplaba Dataview (fase 4) para vistas dentro de Obsidian y `pkos lint` (fase 5) como primer código. La pregunta real era *dónde* construir la primera vista rica: dentro de Obsidian o fuera.

## Alternativas consideradas

### Opción A — Solo Dataview (plan original de fase 4)

- ✅ Barato, vive donde ya se trabaja.
- ❌ No avanza nada hacia la app propia: las queries de Dataview no son transferibles.
- ❌ Interactividad limitada a tablas; un tech radar visual no sale de ahí.

### Opción B — Empezar la app propia (fase 6)

- ❌ Prematuro en todos los frentes: el formato aún evoluciona y no hay lint que garantice datos limpios.

### Opción C — Script generador de una vista derivada *(elegida)*

- ✅ `tools/pkos_stats.py` parsea el vault según `docs/02-data-model.md` y genera un HTML autocontenido: **el parser es el embrión literal de `pkos lint` (fase 5) y de la app (fase 6)** — un esfuerzo, tres frutos.
- ✅ Sin dependencias obligatorias (PyYAML opcional con fallback propio): corre en cualquier Python.
- ✅ Respeta la arquitectura: la salida es 100% derivada y desechable; no se versiona.
- ❌ Adelanta parcialmente la fase 5 alterando el orden del roadmap: coste aceptado y documentado aquí.

## Decisión

El código de herramientas vive en `tools/` (por rama, como manda `docs/05-git-workflow.md`). `pkos_stats.py` incluye un mini-lint (wikilinks rotos, frontmatter inválido contra los enums, huérfanas, notas frías) que será extraído a `pkos lint` en la fase 5. Su salida (`tools/out/`) queda gitignoreada: las vistas derivadas se regeneran, no se versionan. Dataview (fase 4) sigue vigente para vistas *dentro* de Obsidian; no compiten.

## Consecuencias esperadas

- Primera verificación programática del contrato: ya cazó un defecto real (`[[Wikilinks]]` sin backticks en DEC-0002) y enseñó dos reglas que el lint necesitará (ignorar código inline y pipes escapados en tablas).
- El contrato de datos tiene ahora un espejo en código (enums duplicados en el script): si el schema cambia, hay que actualizar ambos — fricción que la fase 5 resolverá con JSON Schemas como fuente única.

## Lecciones aprendidas

- (pendiente — revisar cuando se construya `pkos lint`)
