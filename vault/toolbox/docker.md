---
type: tool
title: Docker
created: 2026-07-12
updated: 2026-07-12
status: evaluating
category: devops
problem: Empaquetar una aplicación con todas sus dependencias en contenedores que corren igual en cualquier máquina — el fin del "en mi máquina funciona"
alternatives: [Podman]
integrates-with: ["[[vscode]]", "[[postgresql]]", "[[mysql]]", "[[mongodb]]"]
url: https://www.docker.com
docs: https://docs.docker.com
tags: [topic/devops]
aliases: []
---

# Docker

## Cuándo usarla

- Levantar servicios de desarrollo (bases de datos, colas) sin instalarlos en el sistema: `docker run postgres` y listo.
- Garantizar que desarrollo, CI y producción ejecutan exactamente el mismo entorno.

## Cuándo NO usarla

- Proyectos de un solo archivo o scripts: contenedorizar todo por principio es sobre-ingeniería.
- Apps de escritorio con GUI: no es su modelo.

## Ventajas

- Reproducibilidad: el `Dockerfile` es el entorno documentado como código.
- Aislamiento: cada proyecto con sus versiones de todo, sin contaminar el sistema.
- Estándar absoluto de la industria: requisito en casi cualquier oferta de backend/devops.

## Desventajas

- Curva conceptual real: imágenes vs contenedores vs volúmenes vs redes lleva tiempo asentarse.
- En Windows requiere WSL2 y consume recursos notables.
- Fácil de usar por cargo cult (copiar Dockerfiles sin entenderlos) — el objetivo del aprendizaje es evitarlo.

## Ejemplos de uso propios

<!-- pendiente: primer caso de uso real — buen candidato: levantar postgres para un proyecto -->

## Notas de experiencia

- **En aprendizaje (2026-07-12)** — por eso `status: evaluating`. Pasará a `adopted` cuando lo use con soltura en un proyecto real. Plan de estudio activo: [[plan-docker]].
