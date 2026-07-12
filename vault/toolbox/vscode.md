---
type: tool
title: Visual Studio Code
created: 2026-07-12
updated: 2026-07-12
status: adopted
category: app
problem: Editor de código universal — un solo editor con extensiones para cualquier lenguaje, con LSP, debugging y Git integrados
alternatives: [JetBrains IDEs, Neovim, Zed]
integrates-with: ["[[git]]", "[[typescript]]", "[[python]]", "[[docker]]", "[[claude-ai]]"]
url: https://code.visualstudio.com
docs: https://code.visualstudio.com/docs
tags: [topic/tooling]
aliases: [VS Code, VSCode]
---

# Visual Studio Code

## Cuándo usarla

- Editor por defecto para todo: la relación capacidad/configuración/precio no la iguala nadie.
- Stacks múltiples (como el mío): un editor que cubre Python, JS/TS, Java, C# y C++ con extensiones oficiales.

## Cuándo NO usarla

- Proyectos Java/C# muy grandes donde un IDE completo (IntelliJ, Rider) da refactoring más profundo.

## Ventajas

- Ecosistema de extensiones gigante y protocolo LSP: el soporte de lenguajes es plugin, no producto.
- Terminal, debugging y Git integrados: el ciclo completo sin salir del editor.
- Gratis, multiplataforma, y el estándar de facto — cualquier tutorial lo asume.

## Desventajas

- Electron: consumo de memoria alto frente a editores nativos.
- Microsoft: las mejores extensiones (Pylance, C#) son propietarias aunque el core sea open source.
- La configuración por proyecto (`.vscode/`) tienta a acoplar el repo al editor — en el PKOS aplica la misma regla que Obsidian: comodidad sí, dependencia no.

## Ejemplos de uso propios

- Edición del propio PKOS (junto a [[obsidian]] para la navegación por enlaces).

## Notas de experiencia

- Primera herramienta con `category: app` tras la [[DEC-0005-ampliar-enum-category|DEC-0005]].
