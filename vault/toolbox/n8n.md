---
type: tool
title: n8n
created: 2026-07-12
updated: 2026-07-12
status: evaluating
category: service
problem: Automatizar flujos entre servicios (APIs, RSS, webhooks, archivos) con workflows visuales, self-hosted y sin escribir un backend por cada integración
alternatives: [Zapier, Make, GitHub Actions, scripts propios con cron]
integrates-with: ["[[docker]]"]
url: https://n8n.io
docs: https://docs.n8n.io
tags: [topic/tooling, topic/automatizacion]
aliases: []
---

# n8n

## Cuándo usarla

- Pipelines de integración con varias fuentes y transformaciones (el caso del Radar: RSS + APIs → filtro → Markdown).
- Cuando quieres automatización *self-hosted*: tus datos y credenciales no pasan por un SaaS de terceros.

## Cuándo NO usarla

- Una sola tarea simple y estable: un script de 30 líneas con cron es menos infraestructura que mantener n8n vivo.
- Automatización ligada a un repo (CI): GitHub Actions ya vive donde está el código.

## Ventajas

- Self-hosted con [[docker]]: gratis, privado, y controlas exactamente qué corre y cuándo.
- Nodos listos para cientos de servicios + nodos de código (JS) para lo que falte.
- Los workflows son JSON exportable: versionables y portables (filosofía compatible con el PKOS).

## Desventajas

- Es un servicio más que operar: actualizaciones, backups de sus workflows, uptime.
- La lógica compleja en nodos visuales se vuelve difícil de leer y depurar antes de lo que parece.
- Los nodos de IA hacen trivial conectar un LLM a todo — justo el riesgo de gasto que [[DEC-0006-radar-de-descubrimiento|DEC-0006]] acota por diseño.

## Ejemplos de uso propios

- (planificado) Fase B del Radar: recolección semanal de fuentes → digest en `vault/_inbox/` ([[DEC-0006-radar-de-descubrimiento|DEC-0006]]).

## Notas de experiencia

- En evaluación (2026-07-12): pasará a `adopted` cuando el ritual manual del Radar valide el formato y n8n lo automatice de verdad.
