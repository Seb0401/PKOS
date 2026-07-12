# PKOS — Personal Knowledge Operating System

Sistema personal para gestionar conocimiento, proyectos, aprendizaje y herramientas a lo largo de toda una carrera profesional.

## Principio rector

> **Los datos son el sistema; las aplicaciones son intercambiables.**

La base de conocimiento vive en archivos Markdown planos con metadatos YAML. Hoy la interfaz es [Obsidian](https://obsidian.md); mañana puede ser una aplicación propia (web, escritorio o móvil) que lea exactamente los mismos archivos. Nada en la estructura de datos depende de Obsidian.

## Módulos

| Módulo | Propósito |
|---|---|
| **Workspace** | Proyectos: documentación, tareas, decisiones técnicas, stack, cronología e ideas. |
| **Learning Hub** | Planes de estudio, certificaciones, recursos, progreso y roadmaps de aprendizaje. |
| **Toolbox** | Biblioteca personal de herramientas: cuándo usarlas, qué resuelven, alternativas e integraciones. |
| **Decision Journal** | Registro de decisiones importantes: contexto, alternativas, decisión final y lecciones. |

## Estructura del repositorio

```
PKOS/
├── docs/          Especificación del sistema (arquitectura, modelo de datos, convenciones)
├── vault/         La base de conocimiento (esto es lo que abre Obsidian)
│   ├── workspace/
│   ├── learning/
│   ├── toolbox/
│   ├── decisions/
│   ├── _inbox/      Digests del Radar pendientes de triage (DEC-0006)
│   └── _templates/
├── tools/         Scripts que derivan vistas del vault (pkos_stats.py → HTML)
├── CLAUDE.md      Contexto para sesiones de trabajo con IA
└── README.md
```

## Empezar aquí

1. [`docs/00-vision.md`](docs/00-vision.md) — qué es el PKOS y qué no es.
2. [`docs/01-architecture.md`](docs/01-architecture.md) — arquitectura y principios de diseño.
3. [`docs/02-data-model.md`](docs/02-data-model.md) — el contrato de datos (schemas de frontmatter).
4. [`docs/03-conventions.md`](docs/03-conventions.md) — nomenclatura, enlaces y etiquetas.
5. [`docs/04-roadmap.md`](docs/04-roadmap.md) — fases de construcción.
6. [`docs/05-git-workflow.md`](docs/05-git-workflow.md) — ramas, commits y flujo de trabajo.

## Estado

**Fase 0 — Fundamentos.** Diseño del sistema y documentación viva. Aún no hay código: el contrato de datos se estabiliza antes de construir nada encima.
