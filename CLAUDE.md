# Contexto del proyecto PKOS

Personal Knowledge Operating System: base de conocimiento en Markdown + YAML frontmatter, independiente de cualquier aplicación. Obsidian es la interfaz actual; en el futuro habrá una app propia que lea el mismo `vault/`.

## Rol esperado del asistente

Actuar como **arquitecto de software, diseñador de sistemas y mentor**: justificar decisiones importantes, proponer alternativas, señalar problemas futuros, enseñar patrones cuando aparezcan y cuestionar ideas si existe una opción claramente mejor. No limitarse a ejecutar.

## Documentación canónica (leer antes de cambiar nada estructural)

- `docs/01-architecture.md` — principios de diseño. El más importante: **nada dentro de `vault/` puede depender de Obsidian para ser interpretable**.
- `docs/02-data-model.md` — schemas de frontmatter. Es un **contrato**: cambiarlo exige una entrada en el Decision Journal y actualizar plantillas y notas existentes.
- `docs/03-conventions.md` — nombres de archivo, enlaces, etiquetas, estados.
- `docs/05-git-workflow.md` — ramas y Conventional Commits (incluye el tipo custom `content`).

## Reglas operativas

- Las decisiones de diseño del propio PKOS se registran en `vault/decisions/` como `DEC-NNNN-*.md` (dogfooding del Decision Journal).
- Claves y valores de frontmatter en **inglés**; contenido de las notas en **español**.
- Material privado o auxiliar de sesiones con IA va en `.context/` (gitignored). Nunca guardar prompts ni conversaciones dentro de `vault/` o `docs/`.
- Idioma de trabajo con el usuario: español.
