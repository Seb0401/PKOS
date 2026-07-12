---
type: tool
title: Playwright
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: testing
problem: Tests end-to-end en navegadores reales (Chromium, Firefox, WebKit) — verificar la app como la usa un humano, automatizado
alternatives: [Cypress, Selenium]
integrates-with: ["[[typescript]]", "[[nextjs]]", "[[vitest]]"]
url: https://playwright.dev
docs: https://playwright.dev/docs/intro
tags: [topic/testing]
aliases: []
---

# Playwright

## Cuándo usarla

- Verificar flujos completos de usuario (login → acción → resultado) en el navegador de verdad.
- Cuando el bug solo aparece "en la app real" y los tests unitarios no lo ven.

## Cuándo NO usarla

- Lógica pura: los E2E son lentos y frágiles comparados con [[vitest]] — la pirámide de tests existe por algo (muchos unitarios, pocos E2E).

## Ventajas

- Los tres motores de navegador con una sola API, paralelismo real sin tier de pago.
- Auto-waiting: espera a que los elementos estén listos, eliminando la mayor fuente de flakiness.
- Codegen y trace viewer: graba interacciones y reproduce fallos paso a paso.

## Desventajas

- Suite E2E grande = minutos de CI; hay que curar qué merece ser E2E.
- Los selectores acoplados al DOM se rompen con cada rediseño (mitigación: `data-testid`).

## Ejemplos de uso propios

- [[methodlife]]: tests end-to-end del core.

## Notas de experiencia

- Promovida del Radar 2026-07-12: ya la usaba sin tenerla en el radar.
