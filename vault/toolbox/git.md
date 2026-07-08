---
type: tool
title: Git
created: 2026-07-07
updated: 2026-07-07
status: adopted
category: devops
problem: Control de versiones distribuido — historial completo, ramificación barata y sincronización entre máquinas para cualquier proyecto basado en archivos
alternatives: []
integrates-with: ["[[obsidian]]", "[[markdown]]"]
url: https://git-scm.com
docs: https://git-scm.com/doc
tags: [topic/devops]
aliases: []
---

# Git

## Cuándo usarla

- Cualquier proyecto de código, sin excepción.
- Bases de conocimiento en texto plano (como este vault): historial, backup y sincronización gratis.
- Documentos importantes que evolucionan (specs, CVs, configuraciones).

## Cuándo NO usarla

- Archivos binarios grandes o que cambian constantemente (vídeo, PSDs): el repo engorda sin diffs útiles. Para eso, Git LFS o almacenamiento normal con backup.
- Colaboración en tiempo real sobre el mismo documento (Git es asíncrono por diseño).

## Ventajas

- Estándar absoluto de la industria: conocimiento transferible a cualquier equipo y tooling infinito.
- Distribuido: el historial completo vive en cada clon — no hay punto único de fallo.
- El historial bien cuidado (Conventional Commits) es documentación gratuita.

## Desventajas

- Curva de aprendizaje real a partir de lo básico (rebase, reflog, resolución de conflictos).
- CLI con interfaz históricamente inconsistente; los errores de novato pueden asustar (aunque casi todo es recuperable vía `reflog`).

## Ejemplos de uso propios

- Este repositorio: trunk-based + Conventional Commits con tipo custom `content` (ver `docs/05-git-workflow.md`).
- `git log --oneline --grep="^feat\|^docs"` — ver solo la evolución estructural del PKOS, filtrando el ruido de contenido.

## Notas de experiencia

- `git add --renormalize .` tras añadir `.gitattributes` a un repo existente evita diffs fantasma de finales de línea (aplicado aquí el 2026-07-07).
