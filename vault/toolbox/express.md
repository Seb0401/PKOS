---
type: tool
title: Express
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: framework
problem: Framework web minimalista para Node.js — routing, middleware y manejo de peticiones HTTP sin imponer estructura
alternatives: [Fastify, NestJS, Hono]
integrates-with: ["[[nodejs]]", "[[mongodb]]", "[[postgresql]]", "[[mysql]]"]
url: https://expressjs.com
docs: https://expressjs.com/es/
tags: [topic/web, topic/backend]
aliases: []
---

# Express

## Cuándo usarla

- APIs REST pequeñas y medianas sobre [[nodejs]]: es el estándar que todo tutorial y todo empleador asume.
- Para aprender backend: su modelo de middleware enseña cómo funciona HTTP sin magia por encima.

## Cuándo NO usarla

- Proyectos grandes de equipo sin arquitectura acordada: su libertad total degenera en caos (NestJS impone estructura).
- Si el rendimiento bruto del servidor es el cuello de botella (Fastify es más rápido).

## Ventajas

- Minimalista y transparente: una petición se sigue con el dedo por la cadena de middleware.
- Madurez y documentación inmensas; cualquier problema ya lo tuvo alguien.

## Desventajas

- No decide nada por ti: validación, autenticación y estructura de carpetas son responsabilidad tuya.
- Desarrollo del core casi congelado durante años; sigue siendo válido, pero la innovación pasa en otros frameworks.

## Ejemplos de uso propios

<!-- pendiente: añadir proyectos o ejercicios concretos donde lo usé -->

## Notas de experiencia

- Nivel autodeclarado (2026-07-12): lo he usado sin considerarme experto.
