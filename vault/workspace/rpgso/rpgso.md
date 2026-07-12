---
type: project
title: RPGSO — Simulador visual de sistemas operativos
created: 2026-07-12
updated: 2026-07-12
status: active
area: personal
started: 2026-07-07
finished:
stack: ["[[typescript]]", "[[vite]]"]
repo: https://github.com/Seb0401/RPGSO
links: []
tags: [topic/sistemas-operativos, topic/simulacion]
aliases: [RPGSO]
---

# RPGSO — Simulador visual de sistemas operativos

## Resumen

Simulador educativo de un sistema operativo que corre en el navegador: un "computador de fantasía" donde scheduler, gestión de memoria, memoria virtual, interrupciones, syscalls y filesystem ejecutan algoritmos reales pero **totalmente observables**. Tiempo simulado (pausable, paso a paso, cámara lenta) y un dashboard —el "Observatorio"— donde los procesos son criaturas con estado y energía y la memoria es territorio explorable.

Arquitectura: núcleo de simulación puro y determinista en [[typescript]], independiente de la UI (la interfaz solo observa el motor). Build con [[vite]], sin framework de servidor — a propósito.

## Objetivos

- Fase 0: núcleo de simulación + observatorio básico.
- 9 fases más planificadas: memoria física → virtual → procesos → scheduling → interrupciones → filesystem → syscalls → ISA propia → escenarios (deadlock, race conditions, starvation).

## Decisiones

<!-- núcleo puro/determinista separado de la UI: mismo patrón que el PKOS (datos ≠ presentación) — candidato a DEC -->

## Tareas

- [ ] Completar fase 0 (núcleo + observatorio)

## Cronología

- 2026-07-12 — Alta en el PKOS. Estado: fase 0, 3 commits.
- 2026-07-07 — Inicio del repositorio.

## Ideas / Backlog

- Los escenarios de fallos clásicos (deadlock, starvation) como material de estudio para el Learning Hub cuando exista un plan de sistemas operativos.

## Enlaces

- Repo: https://github.com/Seb0401/RPGSO
