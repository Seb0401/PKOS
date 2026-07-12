---
type: decision
id: DEC-0005
title: Ampliar el enum category con runtime, app y format
created: 2026-07-12
updated: 2026-07-12
status: accepted
date: 2026-07-12
scope: architecture
context-of: "[[pkos]]"
supersedes:
superseded-by:
tags: [topic/pkos]
aliases: [DEC-0005]
---

# DEC-0005 — Ampliar el enum `category` con `runtime`, `app` y `format`

## Contexto

El enum `category` del schema `tool` nació con 10 valores. La regla acordada fue ajustar el schema solo cuando la ausencia "duela dos veces", y ya dolió:

1. **2026-07-07** — [[obsidian]] (una aplicación de escritorio) y [[markdown]] (un formato de texto) cayeron en `other` por no tener categoría propia. Se registró la fricción sin actuar.
2. **2026-07-12** — al dar de alta el stack real, [[vscode]] (aplicación) y [[nodejs]] (entorno de ejecución: ni lenguaje, ni framework, ni librería) repiten el problema.

Con 4 herramientas sin relación entre sí agrupadas en `other`, la categoría deja de servir para consultar.

## Alternativas consideradas

### Opción A — Mantener `other` como cajón de sastre

- ✅ El enum no cambia; cero migración.
- ❌ `other` ya agrupa editor, formato, runtime y app: una categoría que no discrimina no aporta información.
- ❌ Contradice el propósito del campo: permitir vistas tipo tech radar por categoría.

### Opción B — Convertir `category` en texto libre

- ✅ Flexibilidad total, nunca más una fricción de enum.
- ❌ Deriva inevitable en sinónimos (`editor` / `ide` / `app`) que rompen las consultas.
- ❌ Un enum es un contrato verificable por `pkos lint` (fase 5); texto libre no.

### Opción C — Añadir solo los valores que el dolor observado exige *(elegida)*

- ✅ Cambio **aditivo**, permitido dentro de `schema_version: 1` (ver `docs/02-data-model.md`).
- ✅ Cada valor nuevo responde a casos reales, no a taxonomía especulativa.
- ❌ El enum crecerá con el tiempo; aceptado mientras cada adición pase la regla de "doler dos veces".

## Decisión

El enum `category` del schema `tool` se amplía con tres valores:

- **`runtime`** — entornos de ejecución: Node.js, Deno, JVM.
- **`app`** — aplicaciones con las que se trabaja: Obsidian, VS Code.
- **`format`** — formatos y especificaciones: Markdown, YAML, JSON.

Quedando: `language | framework | database | devops | testing | ai | service | cli | library | runtime | app | format | other`. Se migran las notas afectadas en el mismo cambio: [[obsidian]] → `app`, [[markdown]] → `format`.

## Consecuencias esperadas

- `other` vuelve a significar "de verdad no encaja", que es su único uso legítimo.
- Precedente de proceso: primer cambio real del contrato de datos, ejecutado según sus propias reglas (decisión registrada + migración atómica en rama corta).
- `pkos lint` (fase 5) validará contra el enum ampliado.

## Lecciones aprendidas

- (pendiente de revisión — programada para ~2026-10)
