---
type: tool
title: TypeScript
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: language
problem: Añadir tipado estático a JavaScript para detectar errores en compilación y hacer los contratos entre módulos explícitos
alternatives: ["[[javascript]]"]
integrates-with: ["[[javascript]]", "[[nodejs]]", "[[react]]", "[[vscode]]"]
url: https://www.typescriptlang.org
docs: https://www.typescriptlang.org/docs/
tags: [topic/languages, topic/web]
aliases: [TS]
---

# TypeScript

## Cuándo usarla

- Cualquier proyecto JavaScript que vaya a vivir más de unas semanas o superar un archivo.
- APIs y librerías: los tipos son documentación ejecutable del contrato.

## Cuándo NO usarla

- Scripts desechables de una tarde, donde configurar el compilador cuesta más de lo que aporta.

## Ventajas

- Detecta en el editor errores que JavaScript revelaría en producción.
- Autocompletado y refactoring de [[vscode]] pasan de adivinanza a precisión (mismo autor: Microsoft).
- Es un superconjunto: se adopta gradualmente sobre código JS existente.

## Desventajas

- Paso de compilación y configuración (`tsconfig.json`) que JavaScript puro no necesita.
- El sistema de tipos avanzado (genéricos, condicionales) tiene su propia curva de aprendizaje.
- Los tipos desaparecen en runtime: no valida datos externos por sí solo (hace falta zod o similar).

## Ejemplos de uso propios

<!-- pendiente: añadir proyectos o ejercicios concretos donde lo usé -->

## Notas de experiencia

- Nivel autodeclarado (2026-07-12): conozco la sintaxis y he programado con él; sin dominio experto aún.
