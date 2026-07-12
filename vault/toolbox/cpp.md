---
type: tool
title: C++
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: language
problem: Rendimiento de C con abstracciones de alto nivel (clases, templates, STL) para sistemas grandes donde la velocidad es requisito
alternatives: ["[[c]]"]
integrates-with: []
url: https://isocpp.org
docs: https://en.cppreference.com/w/cpp
tags: [topic/languages]
aliases: ["C++"]
---

# C++

## Cuándo usarla

- Motores de juegos, gráficos, trading de alta frecuencia, simulación: rendimiento extremo con complejidad de dominio alta.
- Programación competitiva: la STL + velocidad lo hacen el estándar en jueces online.

## Cuándo NO usarla

- Todo lo que no exija su rendimiento: la complejidad del lenguaje es de las más altas que existen.

## Ventajas

- Rendimiento al nivel de C con contenedores, algoritmos y RAII que eliminan clases enteras de errores.
- Presente en toda la industria del software de base (navegadores, motores, compiladores).

## Desventajas

- Lenguaje inmenso: décadas de capas acumuladas; dos códigos C++ idiomáticos pueden no parecerse en nada.
- Los errores de memoria siguen siendo posibles, solo más difíciles que en C.
- Tiempos de compilación y tooling (CMake) notoriamente ásperos.

## Ejemplos de uso propios

<!-- pendiente: añadir proyectos o ejercicios concretos donde lo usé -->

## Notas de experiencia

- Nivel autodeclarado (2026-07-12): conozco la sintaxis y he programado con él; sin dominio experto aún.
