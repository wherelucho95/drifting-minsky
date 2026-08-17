# 04 — GitHub Projects

## Situación

Ya tienes issues sueltos (#1, #2, #3…) y PRs abriéndose. Ana pregunta en Slack:
"¿en qué vamos? ¿qué falta para la Release 0.2?". Contar issues a mano no escala.
Necesitas una **vista de planificación** que junte issues y PRs y muestre en qué estado
está cada uno. Eso es **GitHub Projects**.

## Objetivo

- Entender qué es Projects (el "nuevo", basado en tablas) y para qué sirve.
- Crear un project, añadir issues/PRs y organizarlos en **Board / Table / Roadmap**.
- Usar **campos personalizados** (Status, Priority, Iteration…) y **vistas** filtradas.
- Configurar **automatización** (workflows integrados).
- Distinguir Projects de milestones, labels y task lists.

## Qué es GitHub Projects

**GitHub Projects** (la versión moderna, a veces "Projects v2") es una herramienta de
gestión de trabajo tipo hoja de cálculo + tablero, que vive **sobre** tus issues y PRs.
Cada fila del project es un issue, un PR o una **nota suelta (draft)**. No duplica el
issue: lo referencia, y los cambios se sincronizan.

Un project puede pertenecer a:

- Un **usuario** (tus cosas personales), o
- Una **organización** (compartido por el equipo), y puede abarcar **varios repos** a la vez.

> Ojo con el examen: existe el **Projects clásico** (tableros simples ligados a un repo,
> en proceso de retiro) y el **Projects nuevo** (flexible, multi-repo, con campos y
> vistas). Cuando el examen dice "Projects" hoy se refiere al nuevo.

## Crear un project y poblarlo

**Web**: en tu perfil u organización → pestaña **Projects** → **New project** → eliges
una plantilla (Table, Board…) o empiezas en blanco.

Añadir elementos:

- Botón **+ Add item** → pegas la URL de un issue/PR, o escribes texto para crear un
  **draft** (idea que luego conviertes en issue).
- Desde un **issue**, barra lateral **Projects** → lo agregas al tablero.

Con `gh` (extensión de projects):

```bash
gh project list --owner @me
gh project item-add <número> --owner @me --url https://github.com/<user>/drifting-minsky/issues/1
```

## Las tres vistas (layouts)

Un mismo project se ve de tres formas; cambias entre ellas con pestañas:

| Vista | Se parece a | Buena para |
|-------|-------------|-----------|
| **Board** | Un Kanban (columnas Todo / In progress / Done) | Ver el flujo de trabajo de un vistazo |
| **Table** | Una hoja de cálculo (filas y columnas) | Editar muchos campos rápido, agrupar/ordenar |
| **Roadmap** | Un Gantt sobre una línea de tiempo | Planear fechas e **iterations** |

La clave conceptual: **son vistas del mismo conjunto de datos**, no proyectos distintos.
Cambias el layout sin perder nada.

## Campos personalizados (custom fields)

Más allá de lo que trae el issue, un project añade **campos**:

- **Status** — típicamente `Todo / In Progress / Done` (es el que ordena el Board).
- **Text**, **Number**, **Date**.
- **Single select** — lista fija, ej. `Priority: 🔴 High / 🟡 Medium / 🟢 Low`.
- **Iteration** — bloques de tiempo (sprints) con fechas; alimenta el Roadmap.

Ejemplo para `drifting-minsky`: campo `Area` (single select: `ingest / clean / transform
/ aggregate / infra`) para agrupar el trabajo del pipeline.

## Vistas guardadas, filtros e insights

- **Filtrar** con la misma sintaxis que en issues: `status:"In Progress" priority:High
  assignee:@me`.
- **Group by** un campo (ej. agrupar por `Status` o por `Area`).
- **Guardar** cada configuración como una **vista** con nombre (pestañas: "Sprint actual",
  "Bugs", "Roadmap Q3"…).
- **Insights** — gráficos integrados (burn-up, items por estado) para ver tendencias.

## Automatización (built-in workflows)

En **Settings → Workflows** del project activas automatizaciones sin código:

- **Item added to project** → poner `Status = Todo`.
- **Issue/PR closed** → mover a `Done`.
- **Pull request merged** → `Done`.
- **Auto-add** — que cualquier issue nuevo de un repo entre solo al project.

Para lógica más avanzada existe integración con **GitHub Actions** (API de projects),
pero para GH-900 basta con reconocer los workflows integrados.

## Projects vs milestones vs labels vs task lists

Muy preguntado — cada uno tiene su nicho:

| Herramienta | Qué es | Alcance |
|-------------|--------|---------|
| **Label** | Etiqueta de clasificación | Un issue/PR, dentro de un repo |
| **Milestone** | Hito con fecha y % de cierre | Agrupa issues/PRs de **un** repo |
| **Task list** | Checklist dentro de un issue | Subtareas de ese issue |
| **Project** | Tablero/planilla con campos y vistas | Muchos issues/PRs, **multi-repo**, a nivel usuario u org |

Regla: si necesitas **planificar y visualizar** trabajo que cruza repos y estados →
**Project**. Si solo quieres agrupar por entrega dentro de un repo → **milestone**.

## En el examen (GH-900)

- Projects (nuevo) es **flexible y multi-repo**, vive a nivel **usuario u organización**.
- Tres vistas del **mismo** dato: **Board**, **Table**, **Roadmap**.
- Los **campos personalizados** (Status, Iteration, Single select) son lo que lo hace
  potente; **Iteration** alimenta el Roadmap.
- Trae **automatizaciones** integradas (mover a Done al cerrar, auto-add).
- Distingue Project (planificación multi-repo) de **milestone** (agrupación por repo/entrega).
- Un item de project puede ser issue, PR o **draft**.

## Conceptos clave

- **GitHub Projects** — planificación tipo tabla/tablero sobre issues y PRs.
- **Board / Table / Roadmap** — tres vistas del mismo conjunto de items.
- **Custom field** — Status, Priority, Iteration, etc.
- **Built-in workflow** — automatización sin código dentro del project.

## Siguiente

→ [05 — GitHub Actions](05-actions.md)
