---
type: tool
title: JavaScript
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: language
problem: Único lenguaje nativo del navegador; con Node.js cubre también backend, unificando el stack web en un solo lenguaje
alternatives: ["[[typescript]]"]
integrates-with: ["[[nodejs]]", "[[react]]", "[[vscode]]"]
url: https://developer.mozilla.org/es/docs/Web/JavaScript
docs: https://developer.mozilla.org/es/docs/Web/JavaScript
tags: [topic/languages, topic/web]
aliases: [JS]
---

# JavaScript

## Cuándo usarla

- Cualquier cosa que corra en el navegador: no hay alternativa real.
- Backend ligero con [[nodejs]] cuando compartir lenguaje entre front y back simplifica el proyecto.

## Cuándo NO usarla

- Proyectos medianos/grandes sin tipos: ahí [[typescript]] paga su coste con creces.
- Cómputo intensivo o sistemas: no es su nicho.

## Ventajas

- Ubicuo: navegador, servidor, CLIs, apps de escritorio (Electron), móvil (React Native).
- Ecosistema npm gigantesco y comunidad enorme.
- Asincronía nativa (event loop, async/await) bien adaptada a I/O web.

## Desventajas

- Coerciones y peculiaridades históricas (`==`, `this`, hoisting) que producen bugs silenciosos.
- Sin tipos estáticos: los contratos entre módulos viven solo en la cabeza del autor.
- El ecosistema se mueve rápido: fatiga de herramientas y modas.

## Ejemplos de uso propios

<!-- pendiente: añadir proyectos o ejercicios concretos donde lo usé -->

## Notas de experiencia

- Nivel autodeclarado (2026-07-12): conozco la sintaxis y he programado con él; sin dominio experto aún.
