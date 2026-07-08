---
type: decision
id: DEC-0004
title: Historial de main inmutable tras el bootstrap
created: 2026-07-07
updated: 2026-07-07
status: accepted
date: 2026-07-07
scope: process
context-of: "[[pkos]]"
supersedes:
superseded-by:
tags: [topic/pkos, topic/git]
aliases: [DEC-0004]
---

# DEC-0004 — Historial de main inmutable tras el bootstrap

## Contexto

Durante el primer día del repositorio, `main` se reescribió dos veces con force push: primero para eliminar trailers de coautoría (ver [[DEC-0003-autoria-unica-de-commits|DEC-0003]]) y después para compactar 18 micro-commits de arranque en 7 commits temáticos. `docs/05-git-workflow.md` ya declaraba "nunca reescribir main", así que hace falta delimitar cuándo esa regla entra en vigor y con qué excepciones, si alguna.

## Alternativas consideradas

### Opción A — Inmutabilidad absoluta desde el commit inicial

- ✅ Regla sin ambigüedad; los hashes son confiables desde el día uno.
- ❌ Habría fosilizado errores del arranque (trailers no deseados, ruido de 18 micro-commits) sin beneficio real: nadie dependía aún de esos hashes.

### Opción B — Reescritura permitida mientras haya un solo usuario

- ✅ Flexibilidad total en un repo personal.
- ❌ Invita a editar el pasado en lugar de documentarlo, lo contrario del espíritu del Decision Journal.
- ❌ La frontera "un solo usuario" es difusa: clones propios en otras máquinas, CI futura y herramientas que cachean hashes ya cuentan como consumidores del historial.

### Opción C — Ventana de bootstrap con cierre explícito *(elegida)*

- ✅ Permite corregir el arranque en frío (autoría, granularidad) mientras el coste es cero.
- ✅ El cierre queda registrado: esta decisión marca el fin de la ventana; después, la regla es absoluta.
- ❌ Exige disciplina para no reabrir la ventana "solo una vez más".

## Decisión

La ventana de bootstrap queda cerrada con esta decisión. A partir de aquí, `main` es *append-only*: los errores se corrigen hacia adelante con `git revert` o nuevos commits, nunca con `reset`, `rebase`, `filter-branch` ni `push --force` sobre `main`. Las reescrituras quedan permitidas solo en ramas de trabajo aún no fusionadas.

## Consecuencias esperadas

- Los hashes de `main` pasan a ser referencias estables para clones, tags y tooling futuro (`pkos lint`, CI de fase 5).
- Los errores versionados se vuelven visibles en el historial: coherente con la filosofía del sistema (documentar, no borrar).
- Si alguna catástrofe exigiera romper esta regla, requerirá una decisión que la supersea — no una excepción silenciosa.

## Lecciones aprendidas

- (pendiente de revisión — programada para ~2026-10)
