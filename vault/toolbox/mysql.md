---
type: tool
title: MySQL / MariaDB
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: database
problem: Base de datos relacional clásica del stack web; omnipresente en hosting, formación y sistemas legados
alternatives: ["[[postgresql]]"]
integrates-with: ["[[express]]", "[[docker]]"]
url: https://www.mysql.com
docs: https://dev.mysql.com/doc/
tags: [topic/databases]
aliases: [MySQL, MariaDB]
---

# MySQL / MariaDB

## Cuándo usarla

- Proyectos web convencionales (el clásico stack LAMP) y entornos donde ya está desplegada.
- Contextos de formación y empleo local donde es la relacional por defecto.

## Cuándo NO usarla

- Proyecto nuevo sin restricción externa: [[postgresql]] ofrece más por el mismo precio (cero).

## Ventajas

- Ubicua: cualquier hosting barato, cualquier tutorial, cualquier empresa la tiene.
- Sencilla de administrar para casos comunes; réplicas de lectura maduras.
- MariaDB mantiene una alternativa 100% open source y compatible.

## Desventajas

- Menos rigurosa con el estándar SQL y la integridad que PostgreSQL (modos permisivos históricos).
- Menos capacidades avanzadas (tipos ricos, índices sofisticados, extensiones).
- La propiedad de Oracle genera dudas a largo plazo (de ahí el fork MariaDB).

## Ejemplos de uso propios

<!-- pendiente: añadir proyectos o ejercicios concretos donde la usé -->

## Notas de experiencia

- Nivel autodeclarado (2026-07-12): la he usado sin considerarme experto.
