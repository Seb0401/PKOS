---
type: tool
title: Claude (asistente de IA)
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: ai
problem: Asistente de IA para diseñar, programar, revisar y aprender en pareja — multiplicador de productividad y de aprendizaje si se usa con criterio
alternatives: [ChatGPT, Gemini, GitHub Copilot]
integrates-with: ["[[vscode]]", "[[git]]"]
url: https://claude.ai
docs: https://docs.claude.com
tags: [topic/ai, topic/tooling]
aliases: [Claude, Claude Code]
---

# Claude (asistente de IA)

## Cuándo usarla

- Diseño y arquitectura: explorar alternativas con pros/contras antes de decidir (como en este proyecto).
- Aprender: pedir el *porqué* de cada cosa, no solo el código.
- Trabajo mecánico de volumen: scaffolding, migraciones, documentación de base para revisar.

## Cuándo NO usarla

- Como oráculo sin verificación: se equivoca con confianza; todo output importante se revisa.
- Para sustituir la práctica propia: si la IA escribe todo el código, el que no aprende soy yo.

## Ventajas

- Mentor disponible 24/7 que se adapta al nivel y al contexto del proyecto.
- En modo agente (Claude Code) ejecuta tareas completas sobre el repositorio real.
- Reduce el coste de arrancar: el borrador inicial deja de ser la barrera.

## Desventajas

- Riesgo de dependencia: delegar el pensamiento en vez del tecleo.
- Conocimiento con fecha de corte y alucinaciones ocasionales: verificar lo crítico.
- Los límites de uso y precios cambian; no depender de un solo proveedor (las alternativas son intercambiables para la mayoría de tareas).

## Ejemplos de uso propios

- Diseño y construcción del propio PKOS: arquitectura, contrato de datos y este mismo Toolbox.

## Notas de experiencia

- Regla operativa acordada en [[DEC-0003-autoria-unica-de-commits|DEC-0003]]: la IA prepara, el humano revisa y commitea — aplica la misma lógica a cualquier output importante.
- El slug es `claude-ai` y no `claude` a propósito: en filesystems case-insensitive (Windows/macOS), `claude.md` colisiona con la convención `CLAUDE.md` de Claude Code, que lo cargaría como instrucciones del proyecto. Lección: los slugs deben evitar nombres reservados por el tooling.
