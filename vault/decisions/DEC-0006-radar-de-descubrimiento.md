---
type: decision
id: DEC-0006
title: Radar de descubrimiento — pipeline de entrada al Toolbox
created: 2026-07-12
updated: 2026-07-12
status: accepted
date: 2026-07-12
scope: process
context-of: "[[pkos]]"
supersedes:
superseded-by:
tags: [topic/pkos, topic/ai]
aliases: [DEC-0006]
---

# DEC-0006 — Radar de descubrimiento: pipeline de entrada al Toolbox

## Contexto

El PKOS registra bien lo que ya conozco, pero no me ayuda a **descubrir** herramientas, proyectos o tendencias nuevas. El Toolbox ya tiene la semántica correcta para recibirlas (`status: evaluating` = candidata en evaluación, ciclo de tech radar), pero le falta un flujo de entrada. Se quiere automatizar la búsqueda (idea: n8n) **con gasto de tokens controlado y visible** — preocupación explícita: no gastar sin darse cuenta.

## Alternativas consideradas

### Opción A — Sesiones ad-hoc con IA ("¿qué hay de nuevo?")

- ✅ Cero infraestructura.
- ❌ Sin cadencia ni memoria: repite hallazgos, no filtra contra lo ya evaluado/descartado, y el gasto es opaco.

### Opción B — Automatizar todo con IA desde el día uno (n8n + LLM en cada paso)

- ✅ Digest rico y resumido sin esfuerzo.
- ❌ Viola la regla del roadmap ("automatizar solo tras uso real"): se automatiza un proceso que aún no existe.
- ❌ El coste crece silenciosamente — exactamente el riesgo que se quiere evitar.

### Opción C — Pipeline por etapas: recolectar gratis, sintetizar acotado, triar humano *(elegida)*

- ✅ Las fuentes (GitHub Trending por lenguaje, Hacker News, releases de tools adoptadas vía RSS/API) son gratuitas: descubrir no requiere tokens.
- ✅ El LLM solo entra —si entra— en la síntesis, con tope de items, modelo barato y cadencia semanal: gasto acotado por diseño.
- ✅ Se implanta en fases; la automatización llega cuando el proceso manual ya demostró su formato.
- ❌ Requiere el ritual humano de triage; si se abandona, `_inbox/` se convierte en un cementerio (mitigación: el digest es semanal, no diario).

## Decisión

Se añade el flujo **Radar** al PKOS:

1. **`vault/_inbox/`** — carpeta de digests de descubrimiento (`YYYY-MM-DD-radar.md`). Nada en `_inbox/` es fuente de verdad: es materia prima pendiente de triage. Lo que interesa se promueve a `toolbox/<slug>.md` con `status: evaluating`; el resto se borra. Las tools `discarded` funcionan como filtro de exclusión.
2. **Fase A (ya)** — ritual manual: pedir el radar semanal al asistente de IA, que busca en las fuentes y genera el digest. Coste visible por sesión, cero infraestructura.
3. **Fase B** — n8n self-hosted en Docker automatiza solo la *recolección* (fuentes → dedupe contra slugs del Toolbox → digest en `_inbox/`). Sin LLM: cero tokens. n8n **nunca commitea** — extiende [[DEC-0003-autoria-unica-de-commits|DEC-0003]]: toda escritura al historial pasa por revisión humana.
4. **Fase C (opcional)** — nodo LLM de síntesis con presupuesto explícito: modelo económico, máximo de items por corrida, cadencia semanal.

## Consecuencias esperadas

- El Toolbox pasa de registro pasivo a radar con entrada activa; `evaluating` cobra vida real.
- Montar n8n en Docker da propósito concreto al plan de aprendizaje de [[docker]] (Learning Hub, fase 3).
- La arquitectura no se toca: n8n es una app reemplazable más que escribe Markdown estándar — mismo estatus que Obsidian.
- Riesgo aceptado: si el triage se abandona un mes, se pausa la automatización (regla: inbox con >3 digests sin triar = pipeline apagado).

## Lecciones aprendidas

- (pendiente — rellenar tras un mes de ritual manual, antes de construir la fase B)
