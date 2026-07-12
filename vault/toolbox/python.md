---
type: tool
title: Python
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: language
problem: Lenguaje de propósito general con sintaxis mínima para scripts, automatización, backend y ciencia de datos / IA
alternatives: ["[[javascript]]"]
integrates-with: ["[[vscode]]", "[[docker]]"]
url: https://www.python.org
docs: https://docs.python.org/3/
tags: [topic/languages]
aliases: []
---

# Python

## Cuándo usarla

- Scripts y automatización rápida (el "pegamento" universal).
- Prototipos de backend (FastAPI/Django) y todo lo relacionado con datos e IA, donde su ecosistema no tiene rival.
- Buen candidato para el futuro `pkos lint` (fase 5): parseo de YAML/Markdown trivial con librerías maduras.

## Cuándo NO usarla

- Rendimiento crítico o sistemas de bajo nivel (ahí C/C++/Rust).
- Frontend de navegador: no es su terreno.

## Ventajas

- Curva de entrada suave y legibilidad alta: el código se parece al pseudocódigo.
- Ecosistema enorme: hay librería madura para casi cualquier problema.
- Estándar de facto en IA, datos y scripting de infraestructura.

## Desventajas

- Tipado dinámico: los errores de tipo aparecen en ejecución (mitigable con type hints + mypy).
- Gestión de entornos y dependencias históricamente confusa (venv, pip, poetry, uv…).
- Lento frente a lenguajes compilados; irrelevante para scripts, relevante para cómputo pesado.

## Ejemplos de uso propios

<!-- pendiente: añadir proyectos o ejercicios concretos donde lo usé -->

## Notas de experiencia

- Nivel autodeclarado (2026-07-12): conozco la sintaxis y he programado con él; sin dominio experto aún.
