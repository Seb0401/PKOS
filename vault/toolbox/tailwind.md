---
type: tool
title: Tailwind CSS
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: framework
problem: Estilar mediante clases utilitarias en el propio HTML, eliminando la distancia entre el markup y su CSS
alternatives: [CSS plano / CSS Modules, styled-components]
integrates-with: ["[[react]]", "[[nextjs]]", "[[vscode]]"]
url: https://tailwindcss.com
docs: https://tailwindcss.com/docs
tags: [topic/web, topic/frontend]
aliases: [Tailwind]
---

# Tailwind CSS

## Cuándo usarla

- Proyectos de componentes ([[react]]/[[nextjs]]): la co-localización de estilos con el markup encaja natural.
- Prototipado rápido con un sistema de diseño coherente (espaciados, colores y tipografías ya escalados).

## Cuándo NO usarla

- Sin build step o en proyectos donde otro equipo mantiene el CSS con metodologías clásicas (BEM).
- Documentos/contenido de texto largo: ahí CSS semántico clásico es más sano.

## Ventajas

- Elimina la fatiga de nombrar clases y los archivos CSS huérfanos que nadie se atreve a borrar.
- Restricciones de diseño integradas: es difícil producir espaciados inconsistentes.
- Purga automática: el CSS final solo contiene lo usado.

## Desventajas

- HTML ruidoso: filas de 15 clases que dificultan leer la estructura.
- Curva inicial de vocabulario (¿`justify-` o `items-`?) hasta que se automatiza.
- Sin disciplina de componentes, las mismas 15 clases se repiten por todo el proyecto.

## Ejemplos de uso propios

- [[methodlife]] (con componentes propios encima).

## Notas de experiencia

<!-- pendiente: impresiones tras más uso real -->
