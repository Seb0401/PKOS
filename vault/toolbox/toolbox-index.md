---
type: dashboard
title: Toolbox
created: 2026-07-07
updated: 2026-07-12
---

# 🧰 Toolbox

Una herramienta = un archivo plano `toolbox/<slug>.md` (schema `tool`). Sin subcarpetas: la clasificación la dan `category` y los tags. Plantilla: `_templates/tool.md`.

Ciclo de vida (tech radar personal): `evaluating → adopted / discarded → deprecated`. Entrada de candidatas: el Radar ([[DEC-0006-radar-de-descubrimiento|DEC-0006]]).

## 💬 Lenguajes

| Herramienta | Estado | Problema que resuelve |
|---|---|---|
| [[python]] | adopted | Propósito general: scripts, backend, datos e IA |
| [[javascript]] | adopted | Único lenguaje nativo del navegador |
| [[typescript]] | adopted | JavaScript con tipado estático |
| [[java]] | adopted | Backend empresarial con tipado fuerte |
| [[csharp\|C#]] | adopted | Ecosistema .NET: backend, Windows y Unity |
| [[c]] | adopted | Sistemas y base conceptual de la memoria |
| [[cpp\|C++]] | adopted | Rendimiento de C con abstracciones de alto nivel |

## 🌐 Web

| Herramienta | Categoría | Estado | Problema que resuelve |
|---|---|---|---|
| [[react]] | library | adopted | UI como componentes declarativos |
| [[nextjs\|Next.js]] | framework | adopted | Framework full-stack sobre React |
| [[tailwind\|Tailwind]] | framework | adopted | CSS mediante clases utilitarias |
| [[nodejs\|Node.js]] | runtime | adopted | Ejecutar JavaScript fuera del navegador |
| [[express]] | framework | adopted | Framework web minimalista para Node.js |
| [[flask]] | framework | adopted | Microframework web de Python |
| [[vite]] | cli | adopted | Dev server y build de frontend instantáneos |

## 🗄️ Datos

| Herramienta | Categoría | Estado | Problema que resuelve |
|---|---|---|---|
| [[postgresql]] | database | adopted | Relacional open source de referencia |
| [[mysql\|MySQL/MariaDB]] | database | adopted | Relacional clásica del stack web |
| [[mongodb]] | database | adopted | Documental con JSON flexible |
| [[supabase]] | service | adopted | Backend-as-a-service sobre PostgreSQL |

## ⚙️ DevOps y automatización

| Herramienta | Estado | Problema que resuelve |
|---|---|---|
| [[git]] | adopted | Control de versiones distribuido |
| [[docker]] | evaluating | Entornos reproducibles en contenedores |
| [[n8n]] | evaluating | Automatización de flujos self-hosted |

## 🤖 IA

| Herramienta | Estado | Problema que resuelve |
|---|---|---|
| [[claude-ai\|Claude]] | adopted | Asistente de IA para programar y aprender en pareja |

## 🖥️ Apps y formatos

| Herramienta | Categoría | Estado | Problema que resuelve |
|---|---|---|---|
| [[vscode\|VS Code]] | app | adopted | Editor de código universal |
| [[obsidian]] | app | adopted | Interfaz sobre notas Markdown locales |
| [[markdown]] | format | adopted | Texto plano estructurado y longevo |

## Huecos conocidos

- **testing**: categoría vacía — Vitest y Playwright (ya en uso en MethodLife) esperan triage en el Radar.
