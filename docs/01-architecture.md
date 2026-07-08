# Arquitectura

## El patrón central: datos desacoplados de la aplicación

El PKOS aplica el mismo principio que una arquitectura en capas clásica: **la capa de persistencia no conoce a la capa de presentación**.

```
┌─────────────────────────────────────────────────┐
│  Capa de presentación (intercambiable)          │
│  Hoy: Obsidian · Mañana: app propia web/móvil   │
├─────────────────────────────────────────────────┤
│  Capa de acceso (futura)                        │
│  Parser de vault: frontmatter + wikilinks → API │
├─────────────────────────────────────────────────┤
│  Capa de datos (permanente)                     │
│  vault/ — Markdown (CommonMark) + YAML + [[..]] │
└─────────────────────────────────────────────────┘
```

Esto es, en la práctica, un **contrato de interfaz**: cualquier aplicación que quiera consumir el PKOS implementa un parser del formato definido en `02-data-model.md`. Obsidian ya lo implementa "gratis"; la app futura lo implementará explícitamente. Es la misma idea que separar un backend de sus clientes mediante una API: aquí la "API" es el formato de los archivos.

## El formato de datos

Cada nota del vault es:

1. **Frontmatter YAML** — los datos estructurados (el "registro de base de datos"). Es lo que una app consulta, filtra y agrega.
2. **Cuerpo Markdown (CommonMark)** — el contenido humano. Secciones sugeridas por plantilla, pero libres.
3. **Wikilinks `[[nombre]]`** — las relaciones entre notas (las "foreign keys"). Ver DEC-0002 para la justificación frente a enlaces Markdown relativos.

Analogía útil: el vault es una base de datos documental (tipo MongoDB) donde cada nota es un documento, el frontmatter son sus campos indexables y los wikilinks son referencias entre documentos. Pero en texto plano, versionable con Git y legible sin software.

## Reglas arquitectónicas

Estas reglas son normativas. Romperlas exige una decisión registrada (DEC-NNNN).

1. **Fuente de verdad única**: todo el conocimiento vive en `vault/`. Nada importante existe solo en un plugin, una base de datos externa o la cabeza del autor. (Ver DEC-0001.)
2. **Obsidian solo lee y escribe, nunca posee**: los plugins pueden *generar vistas* (Dataview, gráficos) y *facilitar la creación* (Templater, QuickAdd), pero ningún dato queda almacenado en un formato propietario del plugin. Test rápido: si se desinstala el plugin, ¿se pierde información o solo comodidad? Solo puede perderse comodidad.
3. **Markdown estándar en el cuerpo**: se evita sintaxis exclusiva de Obsidian dentro del contenido (callouts y embeds son tolerables porque degradan de forma legible; queries de Dataview embebidas en notas de conocimiento, no — van en dashboards separados y marcados como tales).
4. **Schemas versionados**: `02-data-model.md` declara `schema_version`. Un cambio incompatible incrementa la versión y documenta la migración.
5. **Compatibilidad aditiva**: los campos nuevos son opcionales por defecto. Una nota antigua sin el campo nuevo sigue siendo válida.

## Los cuatro módulos y sus relaciones

```
                    ┌──────────────┐
        usa ------► │   Toolbox    │ ◄------ evalúa
        │           └──────────────┘              │
┌──────────────┐                          ┌──────────────┐
│  Workspace   │ ◄──── genera/consume ──► │   Decision   │
│  (proyectos) │                          │   Journal    │
└──────────────┘                          └──────────────┘
        ▲                                         ▲
        │ motiva                        documenta │
        │           ┌──────────────┐              │
        └---------- │ Learning Hub │ -------------┘
                    └──────────────┘
```

- Un **proyecto** usa herramientas (→ Toolbox), produce decisiones (→ Decision Journal) y puede motivar aprendizaje (→ Learning Hub).
- Una **decisión** referencia el proyecto o plan que la originó y las herramientas que evaluó.
- Un **plan de aprendizaje** puede nacer de un proyecto ("necesito aprender Kubernetes para X") y alimentar el Toolbox con herramientas dominadas.

Las relaciones se materializan siempre como wikilinks en frontmatter o cuerpo — nunca como duplicación de contenido. **Cada hecho vive en un solo sitio y se enlaza desde los demás** (principio DRY aplicado a conocimiento).

## Evolución prevista

- **Fase actual**: Obsidian puro sobre `vault/`.
- **Fase intermedia**: scripts de validación (lint de frontmatter contra los schemas) ejecutables en local o CI. Esto convierte el contrato de datos en algo *verificable*, no solo documentado — y es el primer paso real hacia la app propia, porque obliga a escribir el parser.
- **Fase final**: app propia con capa de acceso (parser → índice → API de consulta) y UI. El vault sigue siendo la única fuente de verdad; la app puede mantener índices derivados (SQLite, etc.) pero siempre reconstruibles desde los archivos.
