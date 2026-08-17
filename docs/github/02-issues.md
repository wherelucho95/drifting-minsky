# 02 — Issues

## Situación

`drifting-minsky` ya está en GitHub. Ana (tu compañera del git-playbook) nota que el
pipeline no valida cantidades negativas en `orders.csv`, y tú quieres proponer una
nueva agregación por país. Nada de esto es código todavía: son **unidades de trabajo**.
En GitHub eso se rastrea con **Issues**.

## Objetivo

- Entender qué es un issue y por qué no es "solo un bug tracker".
- Crear issues con **labels**, **assignees**, **milestones** y **task lists**.
- Usar **plantillas de issue** para estandarizar reportes.
- Cerrar issues automáticamente desde commits/PRs con **closing keywords**.
- Referenciar issues, personas y equipos (`#`, `@`).

## Qué es un issue

Un **issue** es un hilo de trabajo o conversación dentro de un repo: un bug, una tarea,
una idea, una pregunta. Tiene título, descripción (en Markdown), comentarios, y
metadatos (labels, assignee, milestone, project). **No contiene código** — describe
trabajo; el código llega después en un Pull Request que puede cerrar el issue.

Piensa en el issue como el "ticket" y en el PR como "la solución propuesta".

## Crear un issue

**Web**: pestaña **Issues** → **New issue** → título + descripción → **Submit**.

**CLI** con `gh`:

```bash
gh issue create \
  --title "Validar cantidades negativas en orders.csv" \
  --body "read_orders() acepta quantity<0. Deberíamos filtrarlas o marcarlas en clean.py." \
  --label bug --assignee @me
gh issue list                       # ver los abiertos
gh issue view 1                     # ver el detalle del issue #1
gh issue close 1                    # cerrarlo
```

Cada issue recibe un **número** correlativo (`#1`, `#2`, …) único en el repo y
compartido con los PRs (los PRs consumen la misma secuencia de números).

## Metadatos: cómo se organiza el trabajo

En la barra lateral del issue:

- **Assignees** — quién es responsable (una o varias personas).
- **Labels** — etiquetas de color reutilizables. GitHub crea algunas por defecto:
  `bug`, `enhancement`, `documentation`, `good first issue`, `help wanted`,
  `question`, `wontfix`, `duplicate`, `invalid`. `good first issue` y `help wanted`
  son señales para atraer contribuidores externos (caen en el dominio de comunidad).
- **Milestone** — un hito agrupador con fecha opcional (ej. "Release 0.2 — Q3"). Junta
  varios issues y muestra **% de progreso** según cuántos estén cerrados.
- **Projects** — añade el issue a un tablero → [tema 04](04-projects.md).

## Task lists (checklists)

Dentro del cuerpo de un issue puedes desglosar subtareas con `- [ ]`:

```markdown
## Definición de "hecho" para la validación de cantidades
- [x] Detectar `quantity < 0` en `clean.py`
- [ ] Decidir: ¿descartar la fila o marcarla?
- [ ] Añadir test en `tests/test_clean.py`
- [ ] Actualizar el README
```

GitHub muestra una **barra de progreso** (ej. "1 of 4"). Además puedes referenciar
otros issues en una task list para relaciones tipo tarea-madre / subtareas.

## Plantillas de issue (issue templates)

Para que los reportes lleguen completos, defines plantillas en `.github/ISSUE_TEMPLATE/`.
Dos formatos:

- **Markdown clásico**: `.github/ISSUE_TEMPLATE/bug_report.md` con front-matter:

```markdown
---
name: Reporte de bug
about: Algo del pipeline no funciona como debería
title: "[BUG] "
labels: bug
assignees: ""
---

## Qué pasó

## Cómo reproducirlo
1.
2.

## Comportamiento esperado
```

- **Issue Forms (YAML)**: `.github/ISSUE_TEMPLATE/bug.yml` genera un formulario con
  campos obligatorios (más moderno). También existe `config.yml` para, por ejemplo,
  redirigir preguntas a **Discussions** en lugar de abrir un issue.

## Referencias cruzadas: `#`, `@` y closing keywords

- **`#123`** — enlaza al issue/PR número 123. GitHub lo convierte en link y registra
  la relación en ambos lados ("mentioned in").
- **`@usuario`** — menciona a una persona (le notifica).
- **`@org/equipo`** — menciona a un team completo.
- **Closing keywords** — si en la descripción de un **PR** (o en un mensaje de commit)
  escribes una de estas palabras seguida del número, al fusionar el PR el issue se
  **cierra solo**:

  ```
  Closes #12      Fixes #12      Resolves #12
  ```

  (También `close/closed/fix/fixed/resolve/resolved`). Es la forma canónica de atar
  código a la tarea que resuelve. **Muy preguntado en el examen.**

## Otras acciones sobre issues

- **Pin** — fijar hasta 3 issues arriba de la lista.
- **Lock conversation** — congelar comentarios (moderación).
- **Transfer** — mover el issue a otro repo.
- **Convert to discussion** — si era más una conversación que una tarea.
- **Buscar/filtrar** con la sintaxis: `is:issue is:open label:bug assignee:@me
  milestone:"Release 0.2"`.

## En el examen (GH-900)

- Un issue **describe trabajo**, no contiene código; el código va en un **PR**.
- **Labels, milestones, assignees** son los tres organizadores que debes distinguir:
  label = clasificación reutilizable; milestone = hito con % y fecha; assignee = responsable.
- **`Closes #N` / `Fixes #N`** en un PR cierra el issue automáticamente al fusionar.
- Las **task lists** (`- [ ]`) muestran progreso y sirven para planificar.
- `good first issue` y `help wanted` son labels para invitar contribuidores externos.
- Las plantillas viven en `.github/ISSUE_TEMPLATE/`.

## Conceptos clave

- **Issue** — unidad de trabajo/conversación; tiene número único en el repo.
- **Label / Milestone / Assignee** — clasificar / agrupar con fecha / asignar.
- **Task list** — checklist con barra de progreso.
- **Closing keyword** — `Closes/Fixes/Resolves #N` cierra el issue al fusionar el PR.

## Siguiente

→ [03 — Pull Requests y revisiones](03-pull-requests.md)
