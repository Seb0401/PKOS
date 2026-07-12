---
type: tool
title: React
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: library
problem: Construir interfaces de usuario como composición de componentes declarativos que se re-renderizan solos cuando cambia el estado
alternatives: [Vue, Angular, Svelte]
integrates-with: ["[[javascript]]", "[[typescript]]", "[[nodejs]]"]
url: https://react.dev
docs: https://react.dev/learn
tags: [topic/web, topic/frontend]
aliases: []
---

# React

## Cuándo usarla

- SPAs y frontends con estado no trivial, donde manipular el DOM a mano se vuelve inmanejable.
- Cuando el tamaño del ecosistema importa: es la librería de UI con más ofertas de trabajo, componentes y respuestas resueltas.

## Cuándo NO usarla

- Páginas mayormente estáticas: HTML + algo de JS (o Astro) pesa menos y rinde más.
- Proyectos donde el equipo no controla JavaScript: React amplifica lo que ya sabes, incluido lo que no.

## Ventajas

- Modelo mental potente: UI = f(estado); los componentes son funciones componibles.
- Ecosistema dominante: router, formularios, fetching — todo tiene opción madura.
- Transferible: React Native reutiliza el modelo en móvil.

## Desventajas

- Es solo la capa de vista: cada proyecto arrastra decenas de decisiones satélite (router, estado, build).
- Hooks con reglas no evidentes (`useEffect` y dependencias) que producen bugs sutiles al empezar.
- El ecosistema cambia de "manera correcta" cada pocos años (clases → hooks → server components).

## Ejemplos de uso propios

<!-- pendiente: añadir proyectos o ejercicios concretos donde lo usé -->

## Notas de experiencia

- Nivel autodeclarado (2026-07-12): lo he usado sin considerarme experto.
- Candidato natural para el frontend de la futura app del PKOS (fase 6) — evaluar contra opciones más ligeras llegado el momento.
