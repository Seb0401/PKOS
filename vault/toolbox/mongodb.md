---
type: tool
title: MongoDB
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: database
problem: Base de datos documental que almacena JSON flexible sin schema fijo, para datos cuya estructura varía o evoluciona rápido
alternatives: ["[[postgresql]]"]
integrates-with: ["[[express]]", "[[nodejs]]", "[[docker]]"]
url: https://www.mongodb.com
docs: https://www.mongodb.com/docs/
tags: [topic/databases]
aliases: [Mongo]
---

# MongoDB

## Cuándo usarla

- Documentos con estructura genuinamente variable (catálogos heterogéneos, payloads de terceros).
- Prototipos donde el schema aún se está descubriendo y el stack es JavaScript (encaja natural con [[nodejs]]).

## Cuándo NO usarla

- Datos relacionales de verdad (usuarios-pedidos-facturas): modelar relaciones en documentos duele siempre.
- Cuando la integridad transaccional es central: lo relacional lo hace mejor y desde hace décadas.

## Ventajas

- Modelo documento = objeto JavaScript: sin capa de traducción mental en el stack MERN.
- Escalado horizontal (sharding) diseñado desde el origen.
- Onboarding rápido: insertar y consultar JSON sin definir nada antes.

## Desventajas

- "Sin schema" significa que el schema vive implícito en el código — la disciplina que la BD no exige la tiene que poner el equipo (mismo argumento que motivó el frontmatter estricto del PKOS).
- Licencia SSPL: ya no es open source clásico.
- Su flexibilidad inicial se paga en integridad y migraciones al madurar el producto.

## Ejemplos de uso propios

<!-- pendiente: añadir proyectos o ejercicios concretos donde la usé -->

## Notas de experiencia

- Nivel autodeclarado (2026-07-12): la he usado sin considerarme experto.
