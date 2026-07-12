---
type: tool
title: Flask
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: framework
problem: Microframework web de Python — HTTP, routing y templates con lo mínimo, dejando cada decisión de arquitectura al proyecto
alternatives: [FastAPI, Django]
integrates-with: ["[[python]]", "[[mysql]]", "[[postgresql]]"]
url: https://flask.palletsprojects.com
docs: https://flask.palletsprojects.com
tags: [topic/web, topic/backend]
aliases: []
---

# Flask

## Cuándo usarla

- Aplicaciones web de servidor clásicas (templates Jinja2) de tamaño pequeño/medio en [[python]].
- Aprender backend sin magia: cada pieza (ORM, auth, formularios) se elige y entiende por separado.

## Cuándo NO usarla

- APIs nuevas centradas en JSON: FastAPI da validación, tipos y documentación automática por el mismo esfuerzo.
- Proyectos grandes con prisa: Django trae resuelto lo que Flask obliga a ensamblar.

## Ventajas

- Minimalismo real: el "hola mundo" cabe en 5 líneas y no hay nada oculto.
- Ecosistema maduro de extensiones (SQLAlchemy, Flask-Login) que se añaden solo si hacen falta.
- Jinja2: templating potente que además es el mismo motor de medio ecosistema Python.

## Desventajas

- La libertad total significa que la arquitectura (blueprints, capas) es responsabilidad del autor.
- Sin async nativo de primera clase: para I/O concurrente pesado, FastAPI encaja mejor.

## Ejemplos de uso propios

- [[tracereq]]: Flask + SQLAlchemy + [[mysql]], organizado en blueprints.

## Notas de experiencia

<!-- pendiente: impresiones tras más uso real -->
