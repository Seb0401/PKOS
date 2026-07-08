# Modelo de datos

`schema_version: 1`

Este documento es el **contrato de datos** del PKOS. Cualquier aplicación (Obsidian con Dataview hoy, la app propia mañana) debe poder interpretar el vault leyendo únicamente lo definido aquí. Cambiarlo exige una entrada en el Decision Journal.

## Convenciones generales del frontmatter

- Claves y valores enumerados en **inglés** (kebab-case en valores compuestos): el frontmatter es una interfaz para código, y el código se escribe en inglés. El contenido humano de las notas va en español.
- Fechas en formato **ISO 8601** (`YYYY-MM-DD`), sin excepciones — es ordenable, no ambiguo y parseable en cualquier lenguaje.
- Campos marcados ⭐ son obligatorios; el resto, opcionales. **Principio aditivo**: nunca se elimina ni renombra un campo dentro de la misma `schema_version`; solo se añaden opcionales.
- Las relaciones se expresan como wikilinks entre comillas: `project: "[[pkos]]"`. Las listas, como listas YAML.

### Campos comunes a todos los tipos

```yaml
type: project | learning-plan | tool | decision   # ⭐ discriminador del tipo
title: Título legible                              # ⭐
created: 2026-07-07                                # ⭐
updated: 2026-07-07                                # ⭐ tocar al editar significativamente
status: <ver ciclo de vida de cada tipo>           # ⭐
tags: []                                           # taxonomía transversal (ver 03-conventions)
aliases: []                                        # nombres alternativos para enlazado
```

El campo `type` es el discriminador que permite a un parser tratar el vault como colecciones tipadas — el equivalente al nombre de la tabla en una BD relacional.

---

## `project` (Workspace)

Carpeta por proyecto: `vault/workspace/<slug>/`, con la nota principal `<slug>.md` y notas satélite libres (specs, reuniones, ideas) dentro de la carpeta.

```yaml
type: project
status: idea | active | paused | done | archived
area: work | personal | oss | freelance
started: 2026-07-07
finished:                       # vacío hasta que aplique
stack: ["[[python]]", "[[postgresql]]"]   # wikilinks a Toolbox
repo: https://github.com/...
links: []                       # URLs relevantes (docs, staging, tickets)
```

Cuerpo sugerido (ver plantilla): Resumen · Objetivos · Decisiones (lista de `[[DEC-NNNN]]`) · Tareas (checkboxes Markdown) · Cronología (log con fechas, el `updated` de grano fino) · Ideas / Backlog · Enlaces.

**Por qué las tareas son checkboxes y no entidades**: `- [ ] tarea` es Markdown estándar, parseable de forma trivial, y evita crear un archivo por tarea (fricción letal). Si algún día se necesita metadatos por tarea, se extenderá con el formato `- [ ] tarea 📅 2026-01-01` estilo Tasks, que sigue siendo texto plano.

## `learning-plan` (Learning Hub)

Carpeta por plan: `vault/learning/<slug>/`, nota principal + notas de estudio satélite.

```yaml
type: learning-plan
status: planned | in-progress | done | abandoned
goal: Frase que define "terminado"        # criterio de éxito medible
certification: AWS SAA-C03                # si aplica
deadline: 2026-12-01                      # si aplica (ej. fecha de examen)
related-project: "[[slug]]"               # proyecto que motiva el aprendizaje
```

Cuerpo sugerido: Motivación · Roadmap (etapas como checkboxes anidados) · Recursos (tabla: recurso, tipo, estado) · Registro de progreso (log fechado) · Notas y descubrimientos.

**`abandoned` es un estado legítimo**: registrar por qué se abandonó un plan vale tanto como completarlo — es materia prima del Decision Journal.

## `tool` (Toolbox)

Archivo plano: `vault/toolbox/<slug>.md`. Sin subcarpetas: la clasificación la da `category` y los tags, no el filesystem (las carpetas obligan a una jerarquía única; los metadatos permiten N clasificaciones simultáneas).

```yaml
type: tool
status: evaluating | adopted | deprecated | discarded
category: language | framework | database | devops | testing | ai | service | cli | library | other
problem: Qué problema resuelve, en una frase     # ⭐ el campo más valioso del Toolbox
alternatives: ["[[otra-tool]]"]
integrates-with: ["[[otra-tool]]"]
url: https://...
docs: https://...
```

Cuerpo sugerido: Cuándo usarla / Cuándo NO · Ventajas · Desventajas · Ejemplos de uso propios · Notas de experiencia real (esto la distingue de la documentación oficial: aquí va *tu* experiencia).

El ciclo `evaluating → adopted/discarded → deprecated` convierte el Toolbox en un [tech radar](https://www.thoughtworks.com/radar) personal.

## `decision` (Decision Journal)

Archivo plano: `vault/decisions/DEC-NNNN-<slug>.md`. Formato basado en **ADR (Architecture Decision Records)**, el patrón estándar de la industria para esto, extendido con "lecciones aprendidas" porque un journal personal, a diferencia de un ADR de equipo, se revisita.

```yaml
type: decision
id: DEC-0001                    # ⭐ secuencial global, inmutable
status: proposed | accepted | superseded | deprecated
date: 2026-07-07                # fecha de la decisión (created = fecha de la nota)
scope: architecture | tooling | process | career | learning
context-of: "[[pkos]]"          # proyecto o plan que la origina
supersedes: "[[DEC-0003]]"      # si reemplaza a otra
superseded-by:                  # se rellena cuando otra la reemplaza
```

Cuerpo obligatorio (es el tipo más estructurado, a propósito): Contexto · Alternativas consideradas (con pros/contras) · Decisión · Consecuencias esperadas · Lecciones aprendidas (se rellena meses después — programar la revisión es parte del método).

**Por qué ID secuencial global y no por proyecto**: las decisiones se citan entre sí y desde cualquier módulo; un identificador corto, único y estable (`DEC-0042`) es citable de memoria. La numeración por proyecto (`pkos/DEC-3`) rompe la cita cuando una decisión trasciende su proyecto — y las importantes siempre lo hacen.

---

## Validación (futura, fase 5 del roadmap)

Cada schema se formalizará como JSON Schema en `schemas/` y un script validará todo el vault (`pkos lint`). Hasta entonces, este documento + las plantillas de `vault/_templates/` son la única fuente normativa.
