# Flujo de Git

## Estrategia de ramas: trunk-based simplificado

Para un repositorio personal de conocimiento con un solo autor, **git-flow sería sobre-ingeniería** (sus ramas develop/release/hotfix existen para coordinar equipos y despliegues; aquí no hay ninguna de las dos cosas). Se adopta trunk-based con una distinción clave entre *estructura* y *contenido*:

- **`main`** — siempre coherente: la documentación no se contradice, los schemas están completos, no hay plantillas a medias.
- **Contenido directo a `main`**: añadir o editar notas del vault (una tool nueva, un log de progreso, una decisión) se commitea directamente. Es el uso diario; exigir rama para cada nota mataría el sistema por fricción.
- **Rama corta para cambios estructurales**: modificar schemas, convenciones, plantillas o arquitectura — todo lo que afecta a *muchas* notas o al contrato de datos — va en rama `<tipo>/<slug>` (ej. `feat/schema-v2`, `docs/revision-convenciones`) y se fusiona a `main` al completarse, junto con la migración de las notas afectadas. Motivo: un cambio de schema a medias deja el vault en estado inválido, y la rama lo aísla.

Cuando exista código (fase 5+), todo cambio de código va por rama.

## Conventional Commits

Formato: `tipo(ámbito): descripción` — descripción en español, imperativo, sin punto final.

### Tipos

| Tipo | Uso en PKOS |
|---|---|
| `feat` | Nueva capacidad del sistema: plantilla, campo de schema, dashboard, script |
| `fix` | Corregir algo roto: wikilink roto, frontmatter inválido, error en docs |
| `docs` | Documentación del sistema (`docs/`, README, CLAUDE.md) |
| `content` | **Tipo propio**: añadir/editar conocimiento en `vault/` (notas, no estructura) |
| `refactor` | Reorganizar sin cambiar significado: renombrados, movimientos de carpetas |
| `chore` | Mantenimiento: .gitignore, config de Obsidian, dependencias |

**Por qué el tipo custom `content`**: Conventional Commits permite tipos adicionales, y en este repo el 80% de los commits futuros serán conocimiento nuevo, que no es ni `feat` (no cambia el sistema) ni `docs` (no documenta el sistema). Sin este tipo, el historial sería ruido de `docs:` que ocultaría los cambios estructurales reales. Separar `content` permite responder "¿cuándo cambió el sistema?" con `git log --grep` en segundos.

### Ámbitos

`vision` · `architecture` · `data-model` · `conventions` · `roadmap` · `git` · `templates` · `workspace` · `learning` · `toolbox` · `decisions` · `vault` (transversal) · `repo`

Ejemplos:

```
feat(templates): añadir plantilla de learning-plan
content(toolbox): alta de postgresql y redis
content(decisions): DEC-0003 elección de plugin de plantillas
docs(data-model): aclarar formato de fechas en frontmatter
fix(vault): reparar wikilinks rotos tras renombrar docker.md
refactor(toolbox): renombrar categorías según DEC-0007
```

## Plan de commits — Fase 0

Commits pequeños y temáticos: cada uno deja el repo coherente y cuenta un paso de la historia. El historial de un repo es documentación de arquitectura gratuita — merece diseño.

1. `chore(repo): estructura inicial, README y .gitignore`
2. `docs(vision): visión, criterios de éxito y riesgos del PKOS`
3. `docs(architecture): arquitectura en capas y reglas normativas`
4. `docs(data-model): contrato de datos v1 con los cuatro tipos`
5. `docs(conventions): nomenclatura, enlaces y tags`
6. `docs(roadmap): fases 0-6 y criterios de avance`
7. `docs(git): estrategia de ramas y conventional commits`
8. `feat(templates): plantillas de project, learning-plan, tool y decision`
9. `feat(vault): estructura de módulos con índices y home`
10. `content(decisions): DEC-0001 markdown como fuente de verdad`
11. `content(decisions): DEC-0002 wikilinks con nombres únicos`
12. `content(workspace): alta del PKOS como primer proyecto`

Fase 1 seguirá el patrón: un `content(toolbox):` por lote temático de herramientas, un `content(decisions):` por decisión.

## Reglas adicionales

- Commits **atómicos por tema**, no por sesión: "todo lo de hoy" es un anti-patrón que hace inútil el historial.
- `main` se puede reescribir **nunca** (no `push --force`): el historial del PKOS es parte del propio journal.
- Etiquetas `v0.x` al cerrar cada fase del roadmap, para poder citar "el sistema tal como era en la fase N".
