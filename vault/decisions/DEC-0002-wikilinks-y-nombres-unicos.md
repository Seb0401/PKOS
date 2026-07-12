---
type: decision
id: DEC-0002
title: Wikilinks con nombres de archivo únicos para las relaciones
created: 2026-07-07
updated: 2026-07-07
status: accepted
date: 2026-07-07
scope: architecture
context-of: "[[pkos]]"
supersedes:
superseded-by:
tags: [topic/pkos]
aliases: [DEC-0002]
---

# DEC-0002 — Wikilinks con nombres de archivo únicos para las relaciones

## Contexto

Las notas del vault se referencian entre sí constantemente (proyecto → herramientas, decisión → proyecto…). Hay que elegir la sintaxis de enlace, sabiendo que `[[wikilink]]` no es parte de CommonMark — es la única desviación relevante del estándar que usa el PKOS, así que merece decisión explícita.

## Alternativas consideradas

### Opción A — Enlaces Markdown relativos (`[texto](../toolbox/docker.md)`)

- ✅ 100% CommonMark; renderizan en GitHub y en cualquier visor.
- ❌ Frágiles: mover o renombrar un archivo rompe todos los enlaces entrantes salvo que un editor los reescriba.
- ❌ Fricción alta al escribir (rutas relativas mentales) e ilegibles en el texto fuente.

### Opción B — Wikilinks `[[slug]]` con nombres únicos en el vault *(elegida)*

- ✅ Fricción mínima al escribir y máxima legibilidad en crudo — crítico para que el sistema se use.
- ✅ Resistentes a mover archivos entre carpetas (el enlace es al nombre, no a la ruta).
- ✅ Trivial de parsear (`\[\[([^\]|]+)(\|[^\]]+)?\]\]`) y soportado por todo el ecosistema PKM (Obsidian, Logseq, Foam, Zettlr, Silver Bullet).
- ❌ No es CommonMark: la app futura necesita ~20 líneas de código para resolverlos. Coste aceptado.
- ❌ Exige unicidad global de nombres de archivo (si hay dos `docker.md`, el enlace es ambiguo).

## Decisión

Relaciones entre notas del vault: wikilinks `[[slug]]` (en frontmatter, siempre entre comillas). Como requisito derivado, **los nombres de archivo son únicos en todo el vault** (regla en `docs/03-conventions.md`). Enlaces externos y enlaces dentro de `docs/`: Markdown estándar.

## Consecuencias esperadas

- El vault no renderiza perfecto en GitHub (los wikilinks se ven como texto). Irrelevante: GitHub no es una interfaz objetivo.
- La futura herramienta `pkos lint` (fase 5) debe verificar unicidad de nombres y detectar wikilinks huérfanos.
- Configurar Obsidian con `Use [[Wikilinks]]` activado y ruta de nuevos enlaces por nombre de archivo.

## Lecciones aprendidas

- (pendiente de revisión — programada para ~2027-01)
