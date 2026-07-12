---
type: tool
title: Node.js
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: runtime
problem: Ejecutar JavaScript fuera del navegador, habilitando backend, CLIs y tooling con un solo lenguaje en todo el stack
alternatives: [Deno, Bun]
integrates-with: ["[[javascript]]", "[[typescript]]", "[[express]]", "[[vscode]]"]
url: https://nodejs.org
docs: https://nodejs.org/docs/latest/api/
tags: [topic/web, topic/backend]
aliases: [Node.js, Node]
---

# Node.js

## Cuándo usarla

- Backend de aplicaciones web cuando ya se domina JavaScript: un solo lenguaje front + back.
- APIs con mucho I/O concurrente (su event loop no bloqueante brilla ahí) y todo el tooling del ecosistema web.

## Cuándo NO usarla

- Cómputo intensivo de CPU: un solo hilo de ejecución se bloquea (ahí Python con librerías nativas, Go, o workers).

## Ventajas

- npm: el registro de paquetes más grande que existe.
- Asincronía nativa ideal para servidores web típicos (mucho esperar red/disco, poco calcular).
- Es también la plataforma de todo el tooling frontend: conocerlo es obligatorio aunque no hagas backend.

## Desventajas

- Modelo de un solo hilo: un cálculo pesado congela el servidor entero.
- La cultura npm de micro-dependencias infla los `node_modules` y amplía la superficie de ataque de supply chain.

## Ejemplos de uso propios

<!-- pendiente: añadir proyectos o ejercicios concretos donde lo usé -->

## Notas de experiencia

- Nivel autodeclarado (2026-07-12): lo he usado sin considerarme experto.
- Primera herramienta del Toolbox con `category: runtime` — su fricción con el enum original motivó la [[DEC-0005-ampliar-enum-category|DEC-0005]].
