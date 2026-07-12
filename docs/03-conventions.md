# Convenciones

Reglas de nomenclatura, enlaces y etiquetas. Son deliberadamente pocas: cada convención añadida es fricción diaria, así que solo entran las que compran portabilidad o consultabilidad.

## Nombres de archivo

- **kebab-case, ASCII, sin espacios ni acentos**: `plan-aws-saa.md`, no `Plan AWS SAA.md`. Motivo: los nombres de archivo son identificadores (los wikilinks los referencian) y acabarán en URLs, rutas de scripts y sistemas case-sensitive. Los espacios y acentos funcionan en Obsidian y explotan en todo lo demás.
- **Únicos en todo el vault** (requisito de DEC-0002): el wikilink `[[postgresql]]` debe resolver sin ambigüedad. Si dos módulos piden el mismo nombre, se prefija por contexto (`plan-docker.md` vs `docker.md`).
- El título legible (con espacios, acentos y mayúsculas) va en `title:` y en `aliases:`; Obsidian muestra alias en los enlaces, así que no se pierde estética.
- Decisiones: `DEC-NNNN-<slug>.md` con NNNN de 4 dígitos (ordena bien hasta 9999 decisiones; a una decisión importante por semana son ~190 años de margen).

## Enlaces

- **Entre notas del vault**: wikilinks `[[slug]]` o `[[slug|texto visible]]`. Justificación completa en DEC-0002.
- **En frontmatter**: siempre entre comillas — `project: "[[pkos]]"` — porque `[[` sin comillas es YAML inválido en muchos parsers.
- **Hacia fuera del vault** (webs, repos): enlaces Markdown estándar `[texto](url)`.
- **Desde `docs/` hacia `docs/`**: enlaces Markdown relativos (docs/ no es parte del vault y debe renderizar en GitHub).

## Tags

Los tags son la taxonomía **transversal** (cruzan módulos); las carpetas son la taxonomía **estructural** (un módulo, un tipo). No se duplican: nada de `#tool` en una nota que ya vive en `toolbox/` con `type: tool`.

- Formato: kebab-case, jerarquía con `/` cuando aporte: `topic/backend`, `topic/cloud/aws`, `lang/python`.
- Empezar con **una sola familia**: `topic/*`. Añadir familias nuevas solo cuando una búsqueda real las eche en falta (las taxonomías especulativas mueren vacías).

## Estados y fechas

- Valores de `status` únicamente los enumerados en `02-data-model.md` — son una enum, no texto libre; un valor inventado rompe cualquier consulta futura.
- Fechas siempre `YYYY-MM-DD`.
- `updated` se toca en ediciones significativas, no en correcciones de erratas (su función es responder "¿está fresca esta nota?").

## Carpetas especiales del vault

| Carpeta | Propósito |
|---|---|
| `_templates/` | Plantillas de cada tipo. El prefijo `_` las agrupa arriba y las excluye visualmente del conocimiento. |
| `_dashboards/` | (futura) Vistas generadas con Dataview. Separadas porque son *derivadas*: se pueden borrar y regenerar; jamás contienen información original. |
| `_attachments/` | Imágenes y adjuntos. Una sola carpeta plana: los adjuntos se referencian desde las notas, no se navegan. |
| `_inbox/` | Digests del Radar de descubrimiento (DEC-0006), `YYYY-MM-DD-radar.md`. Materia prima *pendiente de triage*: nada aquí es fuente de verdad ni sigue los schemas del contrato — `pkos lint` la excluirá. Se vacía al triar. |

## Regla de oro ante la duda

Ante cualquier caso no cubierto: **elegir la opción más aburrida y estándar** (la que entendería un script de 20 líneas en cualquier lenguaje). Si la elección es importante, registrarla como DEC-NNNN y añadirla aquí.
