---
type: tool
title: C
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: language
problem: Lenguaje de sistemas mínimo y cercano al hardware; base conceptual de la memoria, los punteros y casi todos los lenguajes posteriores
alternatives: ["[[cpp]]"]
integrates-with: []
url: https://en.cppreference.com/w/c
docs: https://en.cppreference.com/w/c
tags: [topic/languages]
aliases: []
---

# C

## Cuándo usarla

- Sistemas embebidos, kernels, drivers: donde el control total de memoria es requisito.
- Como herramienta de aprendizaje: entender punteros, stack/heap y compilación explica cómo funcionan todos los demás lenguajes.

## Cuándo NO usarla

- Aplicaciones de negocio, web o scripts: la gestión manual de memoria es coste sin beneficio.

## Ventajas

- Rendimiento y control máximos; sin runtime ni recolector de basura.
- ABI universal: casi todo lenguaje sabe llamar a código C.
- Formativo: lo que se aprende en C ilumina el resto del stack.

## Desventajas

- Gestión manual de memoria: la fuente clásica de bugs de seguridad (buffer overflows, use-after-free).
- Sin abstracciones modernas: todo se construye a mano.

## Ejemplos de uso propios

<!-- pendiente: añadir proyectos o ejercicios concretos donde lo usé -->

## Notas de experiencia

- Nivel autodeclarado (2026-07-12): conozco la sintaxis y he programado con él; sin dominio experto aún.
