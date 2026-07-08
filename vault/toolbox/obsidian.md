---
type: tool
title: Obsidian
created: 2026-07-07
updated: 2026-07-07
status: adopted
category: other
problem: Interfaz de edición, navegación por enlaces y visualización sobre una carpeta local de notas Markdown, sin poseer los datos
alternatives: []
integrates-with: ["[[git]]", "[[markdown]]"]
url: https://obsidian.md
docs: https://help.obsidian.md
tags: [topic/pkm]
aliases: []
---

# Obsidian

## Cuándo usarla

- Como capa de presentación sobre una base de notas Markdown local que se quiere poseer al 100%.
- Cuando la navegación por enlaces bidireccionales aporta valor real (bases de conocimiento relacionales como el PKOS).

## Cuándo NO usarla

- Como *almacén* de datos: regla arquitectónica del PKOS — Obsidian solo lee y escribe, nunca posee (ver [[DEC-0001-markdown-como-fuente-de-verdad|DEC-0001]]).
- Colaboración multiusuario en tiempo real (no es su modelo).

## Ventajas

- Archivos locales en Markdown plano: cero lock-in de datos.
- Ecosistema de plugins enorme (Dataview, Templater, QuickAdd) para construir vistas y automatizaciones.
- Multiplataforma, incluido móvil, sobre la misma carpeta.

## Desventajas

- **No es open source**: si el producto muere o cambia de rumbo, hay que migrar de interfaz (mitigado por diseño: el vault no depende de ella).
- Sintaxis propietaria tentadora (callouts, embeds, queries embebidas) que erosiona la portabilidad si no se disciplina.
- Los plugins de terceros varían en calidad y mantenimiento: cada plugin adoptado es una dependencia.

## Ejemplos de uso propios

- Este vault: config compartida versionada en `vault/.obsidian/` (wikilinks, plantillas en `_templates/`, papelera local); estado volátil (`workspace.json`) fuera de Git.

## Notas de experiencia

- Regla práctica del PKOS para cada plugin nuevo: "si lo desinstalo, ¿pierdo información o solo comodidad?" Solo puede perderse comodidad.
