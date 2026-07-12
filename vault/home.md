---
type: dashboard
title: Home
created: 2026-07-07
updated: 2026-07-12
---

# 🧠 PKOS

> Los datos son el sistema; las aplicaciones son intercambiables.

## Ahora mismo

<!-- Mantenido a mano; en la fase 4 será una query de Dataview. -->

- 🔥 **Foco**: [[plan-docker]] (fundamentos → n8n) y terminar el triage de [[2026-07-12-radar]] (secciones 3-4).
- 📥 **Pendiente de triage**: 1 digest en `_inbox/` (sección 1 ya promovida).
- ⚖️ **Última decisión**: [[DEC-0006-radar-de-descubrimiento|DEC-0006]] — Radar de descubrimiento (accepted).
- 🗺️ **Roadmap**: Fases 0-2 completas · Fase 3 (Learning Hub) arrancada con [[plan-docker]].

## Módulos

| | Módulo | Qué guarda | Estado |
|---|---|---|---|
| 🗂️ | [[workspace-index\|Workspace]] | Proyectos: docs, tareas, cronología, stack | 6 proyectos activos |
| 📚 | [[learning-index\|Learning Hub]] | Planes de estudio, certificaciones, progreso | 1 plan en curso |
| 🧰 | [[toolbox-index\|Toolbox]] | Tech radar personal: herramientas y experiencia | 30 herramientas |
| ⚖️ | [[decisions-index\|Decision Journal]] | Decisiones con contexto, alternativas y lecciones | 6 decisiones |

## Flujos del sistema

- 📡 **Radar** ([[DEC-0006-radar-de-descubrimiento|DEC-0006]]): fuentes externas → digest en `_inbox/` → triage humano → Toolbox como `evaluating`.
- ⚖️ **Decisiones**: se registran al tomarse; "Lecciones aprendidas" se rellena a los 3-6 meses.
- 🧰 **Tech radar**: `evaluating → adopted / discarded → deprecated`.

## Sistema

La especificación vive fuera del vault, en `docs/` del repositorio: visión · arquitectura · modelo de datos · convenciones · roadmap · flujo de git.
