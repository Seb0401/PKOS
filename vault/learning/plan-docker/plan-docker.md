---
type: learning-plan
title: Docker — de "en aprendizaje" a self-hostear n8n
created: 2026-07-12
updated: 2026-07-12
status: in-progress
goal: Self-hostear n8n con Docker Compose para la fase B del Radar, entendiendo cada línea del compose (no cargo cult)
certification:
deadline:
related-project: "[[pkos]]"
tags: [topic/devops]
aliases: [Plan Docker]
---

# Docker — de "en aprendizaje" a self-hostear n8n

## Motivación

[[docker]] está en `evaluating` con la nota honesta "en aprendizaje", y el sistema le acaba de dar un objetivo real: la fase B del Radar ([[DEC-0006-radar-de-descubrimiento|DEC-0006]]) necesita [[n8n]] self-hosted. Aprender con un destino concreto — no "aprender Docker" en abstracto, sino *usar* Docker para algo que quiero tener funcionando. Criterio de éxito medible: n8n corriendo en local vía compose, entendiendo cada decisión del archivo.

## Roadmap

- [ ] **Fundamentos**: imagen vs contenedor vs volumen vs red — poder explicarlos sin mirar
  - [ ] `docker run`, `ps`, `logs`, `exec`, `stop/rm` con contenedores de prueba
  - [ ] Levantar [[postgresql]] en contenedor con volumen persistente (sirve para cualquier proyecto)
- [ ] **Dockerfile propio**: contenedorizar una app pequeña (candidata: [[tracereq]], Flask es ideal para esto)
- [ ] **Docker Compose**: multi-contenedor con red y volúmenes declarados
- [ ] **Meta: [[n8n]] self-hosted** con compose (n8n + su volumen de datos), documentado
- [ ] Cerrar el ciclo: pasar [[docker]] a `adopted` en el Toolbox y registrar las lecciones aquí

## Recursos

| Recurso | Tipo | Estado |
|---|---|---|
| [Docker — Get Started](https://docs.docker.com/get-started/) | docs oficiales | pending |
| [n8n — Docker installation](https://docs.n8n.io/hosting/installation/docker/) | docs oficiales | pending |
| Docker Desktop + WSL2 (ya instalado en Windows) | entorno | pending |

## Registro de progreso

- 2026-07-12 — Plan creado. Estado real: conceptos sueltos, sin práctica sistemática.

## Notas y descubrimientos

<!-- lo que no dicen los tutoriales: errores propios, sorpresas de WSL2, consumo real -->
