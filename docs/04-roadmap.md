# Roadmap

El orden responde a tres criterios, en este orden de prioridad:

1. **Contrato antes que contenido**: el modelo de datos se estabiliza antes de crear notas en masa, porque migrar 500 notas cuesta 100 veces más que migrar 5.
2. **Dependencias entre módulos**: se construye primero lo que los demás referencian (las decisiones y herramientas son *referenciadas por* los proyectos, no al revés).
3. **Valor inmediato y dogfooding**: cada fase produce algo usable *ya*, y el propio desarrollo del PKOS genera el contenido de prueba (sus decisiones, su entrada de Workspace).

## Fase 0 — Fundamentos ✅ (en curso)

- [x] Visión, arquitectura y modelo de datos documentados
- [x] Convenciones y flujo de Git definidos
- [x] Estructura de carpetas del vault y plantillas
- [x] Primeras decisiones registradas (DEC-0001, DEC-0002)
- [ ] Configurar Obsidian sobre `vault/` (plugins mínimos: Templater o plantillas core)
- [ ] PKOS dado de alta como primer proyecto del Workspace

## Fase 1 — Decision Journal + Toolbox

Los dos módulos "hoja" del grafo de dependencias: nadie depende de que existan proyectos para registrar una decisión o catalogar una herramienta, pero los proyectos sí querrán enlazarlas.

- [ ] Validar la plantilla de decisión con 3–5 decisiones reales (del PKOS y de fuera)
- [ ] Poblar el Toolbox con las 10–15 herramientas del stack actual — sin exhaustividad: solo lo que se usa o evalúa hoy
- [ ] Primer ajuste de schemas con la fricción observada (esperada: campos que sobran)

## Fase 2 — Workspace

El módulo más complejo: tiene subestructura (carpeta por proyecto) y enlaza a los otros tres.

- [ ] Migrar los proyectos activos actuales al formato `project`
- [ ] Validar el flujo diario: abrir proyecto → actualizar cronología → gestionar tareas
- [ ] Dashboard de proyectos activos (primera vista Dataview, en `_dashboards/`)

## Fase 3 — Learning Hub

Último módulo porque reutiliza todos los patrones ya validados (carpeta+nota principal del Workspace, recursos que enlazan al Toolbox, decisiones de qué aprender en el Journal).

- [ ] Crear el primer plan de aprendizaje real (idealmente uno con deadline: certificación)
- [ ] Validar el registro de progreso durante 2–4 semanas de uso real
- [ ] Dashboard de aprendizaje activo

## Fase 4 — Capa de experiencia en Obsidian

Solo cuando los cuatro módulos tienen uso real — automatizar un flujo que no se usa es deuda instantánea.

- [ ] Dashboards por módulo (Dataview) y home actualizado
- [ ] Creación rápida (QuickAdd/Templater): nueva tool, nueva decisión, nuevo log de progreso en ≤ 3 clics
- [ ] Revisión periódica: recordatorio de rellenar "lecciones aprendidas" en decisiones con > 3 meses

## Fase 5 — Contrato verificable

El puente hacia la app propia. *Parcialmente adelantada (DEC-0007): `tools/pkos_stats.py` ya parsea el vault contra el contrato e incluye un mini-lint; esta fase lo formaliza.*

- [ ] JSON Schemas formales en `schemas/` (uno por tipo) — hoy los enums viven duplicados en docs y en el script: esta es la deuda que salda
- [ ] CLI `pkos lint`: valida frontmatter, detecta wikilinks rotos y nombres duplicados (extraer del mini-lint de `pkos_stats.py`)
- [ ] (Opcional) CI en GitHub Actions que ejecuta el lint en cada push

## Fase 6 — Aplicación propia

- [ ] Parser del vault → modelo en memoria (reutiliza los schemas de la fase 5)
- [ ] Índice de consulta (SQLite derivado, siempre reconstruible desde los archivos)
- [ ] API de lectura y primera UI (decisión de plataforma: se registrará como DEC-NNNN cuando toque, con los datos de uso real de las fases 1–4)

**Criterio para avanzar de fase**: no fechas, sino uso — se pasa a la siguiente cuando la actual lleva unas semanas usándose sin fricción grave. Un PKOS es un maratón; las fechas artificiales solo generan culpa.
