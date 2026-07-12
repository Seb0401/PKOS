---
type: tool
title: Supabase
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: service
problem: Backend-as-a-service sobre PostgreSQL — base de datos, autenticación, realtime y storage sin construir ni operar un backend propio
alternatives: [Firebase, Appwrite, backend propio con Express]
integrates-with: ["[[postgresql]]", "[[nextjs]]", "[[react]]", "[[typescript]]"]
url: https://supabase.com
docs: https://supabase.com/docs
tags: [topic/web, topic/backend]
aliases: []
---

# Supabase

## Cuándo usarla

- Proyectos que necesitan auth + BD + API ya, con equipo de una persona: elimina semanas de infraestructura.
- Cuando quieres BaaS *sin* renunciar a SQL: debajo hay [[postgresql]] de verdad, consultable y exportable.

## Cuándo NO usarla

- Cuando el objetivo es *aprender* backend: el servicio resuelve justo lo que se quiere practicar.
- Lógica de negocio compleja en servidor: las Edge Functions se quedan cortas frente a un backend propio.

## Ventajas

- PostgreSQL real: sin lock-in de datos (misma filosofía que el PKOS — se puede migrar con `pg_dump`).
- Row Level Security como modelo de autorización declarativo en la propia BD.
- Auth, realtime y storage integrados con SDKs de calidad para JS/TS.

## Desventajas

- RLS es potente pero traicionero: una política mal escrita expone o bloquea datos silenciosamente.
- El tier gratuito pausa proyectos inactivos: sorpresas en demos y side projects.
- Dependencia de un proveedor para auth y realtime, aunque los datos sean portables.

## Ejemplos de uso propios

- [[methodlife]] (BD compartida entre dos repos con permisos read-only para la capa de gamificación — patrón interesante) y [[vibelearning]].

## Notas de experiencia

- El patrón de MethodLife (repo satélite que solo escribe en su tabla `xp_events` y lee eventos del core) es una buena lección de límites de propiedad sobre una BD compartida.
