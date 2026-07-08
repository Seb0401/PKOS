---
type: decision
id: DEC-0003
title: Autoría única de commits — la IA prepara, el humano commitea
created: 2026-07-07
updated: 2026-07-07
status: accepted
date: 2026-07-07
scope: process
context-of: "[[pkos]]"
supersedes:
superseded-by:
tags: [topic/pkos, topic/git]
aliases: [DEC-0003]
---

# DEC-0003 — Autoría única de commits: la IA prepara, el humano commitea

## Contexto

El PKOS se desarrolla en pareja con un asistente de IA que puede ejecutar comandos de [[git]] directamente. Durante la Fase 0 el asistente ejecutó el plan completo de commits (18) con trailers `Co-Authored-By`, cuando la intención era que solo preparara el plan. El registro de contribuciones y la autoría del historial deben reflejar al dueño del sistema, y ejecutar cada commit personalmente es también un punto de revisión: obliga a leer qué se está versionando antes de sellarlo.

## Alternativas consideradas

### Opción A — La IA commitea con coautoría (comportamiento por defecto)

- ✅ Flujo más rápido; cada cambio queda versionado al momento.
- ❌ Diluye la autoría del historial y llena el registro de contribuciones con actividad no ejecutada conscientemente.
- ❌ Elimina el punto de revisión humano previo al commit: los errores se descubren *después* de versionarlos.

### Opción B — La IA commitea sin trailer, como si fuera el humano

- ✅ Historial "limpio" en apariencia.
- ❌ Deshonesto con el propio registro: el commit dice que lo hizo el humano cuando no revisó ni ejecutó nada.

### Opción C — División de responsabilidades: la IA prepara, el humano commitea *(elegida)*

- ✅ Autoría real y única; cada commit pasó por ojos humanos antes de existir.
- ✅ La IA sigue aportando donde da valor: dejar el working tree listo y proponer el mensaje según `docs/05-git-workflow.md`.
- ❌ Más fricción por cambio (aceptada: el commit es justamente el momento de control de calidad).

## Decisión

Todos los commits y pushes del repositorio los ejecuta el autor humano. Los asistentes de IA preparan los cambios en el working tree y proponen el mensaje de commit, pero nunca ejecutan `git commit` ni `git push` salvo petición explícita e inequívoca, y nunca añaden trailers de coautoría.

## Consecuencias esperadas

- El registro de contribuciones y `git blame` reflejan trabajo revisado y ejecutado por el autor.
- El ritmo de commits baja ligeramente; a cambio, cada commit es una revisión consciente.
- Instrucción persistente para los asistentes: registrada fuera del vault (contexto privado), esta decisión es su versión pública y razonada.

## Lecciones aprendidas

- (pendiente de revisión — programada para ~2026-10)
