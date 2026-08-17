# GitHub Foundations (GH-900) — Guía de estudio con Drifting Minsky

El [`git-playbook`](git-playbook.md) te enseña **Git** (la herramienta de línea de
comandos). Esta guía te enseña **GitHub** (la plataforma que envuelve a Git): repos,
issues, pull requests, projects, actions, seguridad y comunidad. Es lo que necesitas
para **aprobar el examen GitHub Foundations (código GH-900)**.

Seguimos usando el mismo proyecto ficticio, `drifting-minsky`, para que cada concepto
tenga un lugar donde aterrizar en vez de ser teoría suelta.

## Qué es la certificación GH-900

- **Nombre**: GitHub Foundations. Es la certificación de entrada del programa oficial
  de certificaciones de GitHub (las otras son Actions, Advanced Security, Admin y Copilot).
- **Formato**: examen de opción múltiple, en línea y supervisado (proctored).
- **Preguntas**: ~60–75 preguntas. **Tiempo**: ~90 minutos. **Aprobar**: alrededor del 70 %.
- **Enfoque**: mide que sepas *para qué sirve* cada pieza de GitHub y *cuándo usarla*,
  no que memorices flags de Git. Muchas preguntas son "¿cuál es la mejor herramienta
  para este escenario?".
- **Referencia oficial** (verifica siempre, los detalles cambian):
  <https://resources.github.com/learn/certifications/> y el *study guide* del examen.

> **Nota honesta**: los porcentajes y el número de preguntas de abajo reflejan los
> objetivos publicados del examen al momento de escribir esto. GitHub ajusta el temario
> con el tiempo — contrasta con el study guide oficial antes de presentar.

## Dominios del examen y dónde estudiarlos aquí

| # | Dominio | Peso aprox. | Tema(s) en esta guía |
|---|---------|-------------|----------------------|
| 1 | Introducción a Git y GitHub | ~22 % | [git-playbook](git-playbook.md) + [01](github/01-repos-y-proyecto.md) |
| 2 | Trabajar con repositorios de GitHub | ~24 % | [01 — Repos y proyecto](github/01-repos-y-proyecto.md) |
| 3 | Funciones de colaboración | ~22 % | [02 — Issues](github/02-issues.md), [03 — Pull Requests](github/03-pull-requests.md), [06 — Colaboración](github/06-colaboracion-comunidad.md) |
| 4 | Desarrollo moderno | ~12 % | [05 — Actions](github/05-actions.md), [08 — Productos y ecosistema](github/08-productos-y-ecosistema.md) |
| 5 | Gestión de proyectos | ~10 % | [04 — Projects](github/04-projects.md), [02 — Issues](github/02-issues.md) |
| 6 | Privacidad, seguridad y administración | ~5 % | [07 — Seguridad y admin](github/07-seguridad-y-admin.md) |
| 7 | Beneficios de la comunidad GitHub | ~5 % | [06 — Colaboración](github/06-colaboracion-comunidad.md), [08 — Productos](github/08-productos-y-ecosistema.md) |

## Los temas de esta guía

| # | Título | Lo que cubre | Dominios GH-900 |
|---|--------|--------------|-----------------|
| [01](github/01-repos-y-proyecto.md) | **Crear el proyecto en GitHub** | Repos, visibilidad, README/LICENSE/.gitignore, clone/fork, `gh`, Markdown | 1, 2 |
| [02](github/02-issues.md) | **Issues** | Crear, labels, milestones, assignees, plantillas, task lists, closing keywords | 3, 5 |
| [03](github/03-pull-requests.md) | **Pull Requests y revisiones** | PR, draft, reviews, merge methods, branch protection, `gh pr` | 3 |
| [04](github/04-projects.md) | **GitHub Projects** | Tableros, tablas, roadmap, campos, vistas, automatización | 5 |
| [05](github/05-actions.md) | **GitHub Actions** | Workflows, triggers, jobs, runners, secrets, Marketplace, CI real | 4 |
| [06](github/06-colaboracion-comunidad.md) | **Colaboración y comunidad** | Discussions, wikis, Pages, gists, notificaciones, InnerSource, Sponsors | 3, 7 |
| [07](github/07-seguridad-y-admin.md) | **Seguridad y administración** | Permisos, teams, orgs, 2FA, branch protection, Dependabot, code/secret scanning | 6 |
| [08](github/08-productos-y-ecosistema.md) | **Productos y ecosistema** | Planes/facturación, Copilot, Codespaces, Packages, Marketplace, Mobile/Desktop/CLI | 4, 7 |
| [09](github/09-simulacro-gh900.md) | **Simulacro GH-900** | Cheat sheet de repaso + 30 preguntas de práctica con respuestas comentadas | Todos |

## Cómo estudiar con esta guía

1. **Haz primero el [git-playbook](git-playbook.md)** hasta al menos el escenario 03.
   El examen asume que entiendes commit / branch / merge / pull / push.
2. **Lee los temas 01→08 en orden.** Cada uno tiene una sección *"En el examen"* con
   los puntos que caen y cómo los redactan.
3. **Practica de verdad en github.com** con un repo tuyo (puede ser este). Crear un
   issue, abrir un PR y ver correr un Action fija los conceptos más que leerlos.
4. **Haz el [simulacro](github/09-simulacro-gh900.md)** al final. Repite los temas donde falles.

## Git vs GitHub — la distinción que más cae

Es la pregunta trampa más común del examen. Ténla clarísima:

| | **Git** | **GitHub** |
|---|---------|-----------|
| Qué es | Sistema de control de versiones distribuido | Plataforma en la nube construida sobre Git |
| Quién lo hizo | Linus Torvalds (2005) | GitHub, Inc. (2008), hoy de Microsoft |
| Dónde vive | En tu máquina (local) | En internet (github.com) |
| Necesita internet | No | Sí (para colaborar) |
| Ejemplos de uso | `commit`, `branch`, `merge` | Issues, Pull Requests, Actions, Projects |

**Regla de oro para el examen**: si el enunciado habla de *comandos* (`add`, `commit`,
`push`) es **Git**. Si habla de *funciones sociales o web* (issues, PR, review, projects,
actions, wiki) es **GitHub**.

## Glosario express (lo que GitHub añade sobre Git)

- **Repository (repo)** — el proyecto: código + historial + issues + PRs + wiki + settings.
- **Issue** — una unidad de trabajo/discusión: bug, tarea, idea. No es código.
- **Pull Request (PR)** — propuesta de fusionar una rama en otra, con revisión y discusión.
- **Fork** — tu copia personal de un repo ajeno, bajo tu cuenta.
- **GitHub Actions** — automatización (CI/CD y más) que corre en respuesta a eventos.
- **GitHub Projects** — tablero/planilla para organizar issues y PRs como tareas.
- **Organization** — cuenta compartida para equipos, con **teams** y permisos.
- **GitHub Pages** — hosting de sitios estáticos directo desde un repo.
- **Gist** — fragmento de código o nota compartible, con su propio mini-repo.
- **Marketplace** — tienda de Actions y Apps que se integran a GitHub.
