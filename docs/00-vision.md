# Visión

## Qué es el PKOS

Un sistema operativo personal de conocimiento: la infraestructura sobre la que se gestiona una carrera profesional completa — proyectos, aprendizaje, herramientas y decisiones — durante décadas, no meses.

La palabra clave es **sistema operativo**: igual que un SO sobrevive a las aplicaciones que corren sobre él, el PKOS debe sobrevivir a las herramientas que lo consumen. Obsidian es la primera "aplicación"; no será la última.

## Qué NO es

- **No es un vault de Obsidian.** Es una base de datos en texto plano que Obsidian sabe abrir. La distinción importa: si un plugin de Obsidian se vuelve imprescindible para *interpretar* los datos (no solo para visualizarlos), el diseño ha fallado.
- **No es un segundo cerebro genérico** (Zettelkasten, PARA, etc. aplicados al pie de la letra). Toma ideas de esos métodos, pero se organiza alrededor de cuatro módulos concretos con schemas definidos, porque los datos estructurados son consultables y los apuntes sueltos no.
- **No es un gestor de tareas diario.** Las tareas viven dentro de los proyectos que las generan; el PKOS no compite con un calendario o un todo-app.

## Criterios de éxito

1. **Portabilidad total**: se puede borrar Obsidian hoy y todo el conocimiento sigue siendo legible, navegable (por enlaces) y parseable (por frontmatter).
2. **Consultabilidad**: preguntas como "¿qué herramientas conozco para X?", "¿por qué elegí Y en el proyecto Z?" o "¿qué certificaciones tengo en curso?" se responden en segundos.
3. **Coste de mantenimiento bajo**: añadir una nota nueva cuesta menos de un minuto usando plantillas. Si mantener el sistema cuesta más que el valor que da, se abandona — este es el modo de fallo número uno de todos los sistemas de conocimiento personal.
4. **Evolución sin migraciones traumáticas**: los schemas pueden crecer (campos nuevos opcionales) sin romper las notas existentes.

## Riesgos identificados

| Riesgo | Mitigación |
|---|---|
| Sobre-ingeniería inicial: diseñar 40 campos que nunca se rellenan | Schemas mínimos; los campos se añaden cuando duele su ausencia, no antes |
| Dependencia silenciosa de plugins de Obsidian | Regla: plugins solo para *ver y crear*, nunca para *almacenar* (ver arquitectura) |
| Abandono por fricción | Plantillas para todo; una nota imperfecta y existente vale más que una perfecta y no escrita |
| Deriva de convenciones con los años | `docs/` es normativo; cambios de convención pasan por el Decision Journal |
