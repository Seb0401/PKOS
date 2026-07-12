---
type: tool
title: Next.js
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: framework
problem: Framework full-stack sobre React — routing, renderizado en servidor, API routes y build en una sola pieza opinionada
alternatives: [Remix, Astro, Vite + React Router]
integrates-with: ["[[react]]", "[[typescript]]", "[[supabase]]", "[[tailwind]]", "[[nodejs]]"]
url: https://nextjs.org
docs: https://nextjs.org/docs
tags: [topic/web, topic/frontend, topic/backend]
aliases: [Next]
---

# Next.js

## Cuándo usarla

- Aplicaciones web completas con [[react]] donde se quiere front + API + build resueltos sin ensamblar piezas.
- Cuando el destino de deploy es Vercel: la integración es de cero fricción.

## Cuándo NO usarla

- SPAs puramente cliente o simuladores (ahí Vite pelado pesa menos — decisión tomada en RPGSO).
- Sitios estáticos simples: Astro genera menos JavaScript.

## Ventajas

- El framework React por defecto de la industria: contratación, tutoriales y ecosistema.
- App Router + Server Components: data fetching en el servidor sin API intermedia manual.
- Convenciones fuertes (rutas por archivos) que eliminan decisiones repetitivas.

## Desventajas

- Acoplamiento a Vercel en las features más nuevas; fuera de Vercel hay fricción.
- El App Router cambió el modelo mental respecto a Pages Router: mucha documentación antigua confunde.
- Magia considerable: cuando algo falla en el build, la caja es bastante negra.

## Ejemplos de uso propios

- [[methodlife]] (Next 15 + App Router + TypeScript estricto), [[vibelearning]] y [[codventure]].

## Notas de experiencia

- Es mi framework más usado en la práctica (3 proyectos activos en 2026) — más que ninguna otra pieza del stack web.
