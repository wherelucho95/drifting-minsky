# 03 — Pull Requests y revisiones

## Situación

Ya tienes el issue #1 ("Validar cantidades negativas"). Creas la rama
`feature/validate-quantities`, escribes el fix en `clean.py` con su test, y la
empujas. Ahora quieres que Ana lo **revise** antes de que entre a `main`. Eso es un
**Pull Request**: el corazón de la colaboración en GitHub.

## Objetivo

- Entender qué es un PR y cómo se relaciona con las ramas de Git.
- Abrir un PR (web y `gh`), incluyendo **draft PRs**.
- Pedir y dar **reviews** (approve / request changes / comment) y usar **CODEOWNERS**.
- Comparar los tres **merge methods** (merge commit, squash, rebase).
- Conectar el PR con la **branch protection** que verá el [tema 07](07-seguridad-y-admin.md).

## Qué es un Pull Request

Un **Pull Request (PR)** es una propuesta de fusionar los commits de una rama (**head**,
p. ej. `feature/validate-quantities`) dentro de otra (**base**, p. ej. `main`). No es
un comando de Git: es una **función de GitHub** que envuelve la comparación de ramas con:

- **Discusión** — comentarios generales y comentarios línea por línea sobre el diff.
- **Reviews** — aprobación formal, solicitud de cambios o comentario.
- **Checks** — resultados de CI (Actions), status de otros bots.
- **Merge** — el botón que integra la rama cuando todo está listo.

> "Pull request" viene del git open source: le pides al mantenedor que "traiga" (pull)
> tus cambios. En GitLab lo llaman *Merge Request*: es lo mismo.

## Flujo completo (rama → PR → merge)

```bash
# 1. Rama a partir de main actualizado
git switch main && git pull
git switch -c feature/validate-quantities

# 2. Trabajas, commiteas
git add src/drifting_minsky/pipelines/clean.py tests/test_clean.py
git commit -m "fix(clean): descartar filas con quantity < 0

Closes #1"

# 3. Empujas la rama
git push -u origin feature/validate-quantities

# 4. Abres el PR
gh pr create --base main --head feature/validate-quantities \
  --title "Validar cantidades negativas" \
  --body "Descarta filas con quantity<0 en clean.py + test. Closes #1"
```

En la web, tras el push aparece un banner **"Compare & pull request"** que hace lo mismo.

El `Closes #1` en el cuerpo hace que, al fusionar, el issue #1 se cierre solo
(closing keyword del [tema 02](02-issues.md)).

## Draft Pull Requests

Si el trabajo no está listo pero quieres feedback temprano o disparar CI:

```bash
gh pr create --draft --title "WIP: validación de cantidades" ...
```

Un **draft PR** no se puede fusionar hasta que lo marques **"Ready for review"**. Sirve
para señalar "esto todavía no lo revises a fondo".

## Reviews (revisiones de código)

Quien revisa abre la pestaña **Files changed**, comenta líneas y al final emite un
**review** con uno de tres veredictos:

- **Approve** — visto bueno.
- **Request changes** — hay que corregir antes de fusionar (bloquea si la protección lo exige).
- **Comment** — feedback sin veredicto vinculante.

Herramientas de review que caen:

- **Comentarios línea a línea** y **suggested changes** (bloque `suggestion` que el
  autor aplica con un clic).
- **Reviewers** solicitados manualmente, o automáticos vía **CODEOWNERS**.
- Con `gh`: `gh pr review 2 --approve` / `--request-changes -b "..."` / `--comment`.
- `gh pr checks 2` muestra el estado de CI; `gh pr merge 2 --squash` fusiona.

### CODEOWNERS

Un archivo `.github/CODEOWNERS` mapea rutas a responsables. Cuando un PR toca esas rutas,
GitHub pide su review automáticamente:

```
# Todo /src lo revisa Ana; los workflows, el equipo de plataforma
/src/                @ana-dev
/.github/workflows/  @mi-org/plataforma
```

## Los tres merge methods

Al pulsar **Merge**, GitHub ofrece tres estrategias (el admin decide cuáles habilita):

| Método | Qué hace en `main` | Historia |
|--------|--------------------|----------|
| **Create a merge commit** | Añade un commit de merge con 2 padres | Conserva todos los commits de la rama |
| **Squash and merge** | Aplasta todos los commits del PR en **uno solo** | Lineal y limpia; 1 PR = 1 commit |
| **Rebase and merge** | Reaplica los commits de la rama sobre `main`, sin merge commit | Lineal, conserva cada commit |

Relación con el git-playbook: *merge* ↔ escenario 04, *rebase* ↔ escenarios 03/04.
**Squash** es el favorito de muchos equipos para mantener `main` legible: un commit por
funcionalidad. Tras fusionar, GitHub ofrece **borrar la rama**.

## Estados y señales de un PR

- **Open / Draft / Merged / Closed** (cerrado sin fusionar ≠ fusionado).
- **Checks** verdes/rojos (CI de Actions).
- **Conversations resolved** — hilos de review marcados como resueltos.
- **"This branch is out-of-date with base"** — hay que actualizar la rama (fetch+rebase
  o el botón "Update branch"), justo el problema del escenario 03 del git-playbook.
- **Merge conflicts** — GitHub avisa y ofrece un editor web para casos simples; los
  complejos se resuelven en local (escenario 05 del git-playbook).

## Cómo se conectan PR y protección de ramas

Los repos serios protegen `main` para que **nada entre sin PR**. La **branch protection**
(la ves en el [tema 07](07-seguridad-y-admin.md)) puede exigir, antes de permitir merge:

- Al menos N approvals.
- Que los **checks** de CI pasen (status checks required).
- Que la rama esté actualizada con base.
- Que se resuelvan todas las conversaciones.
- Revisión obligatoria de **CODEOWNERS**.

Por eso el PR es la puerta: sin él, esas reglas no tendrían dónde aplicarse.

## En el examen (GH-900)

- Un PR **compara y propone fusionar** una rama (head) en otra (base); es función de
  GitHub, no un comando de Git.
- **Draft PR** = no fusionable hasta marcarlo "ready".
- Los tres veredictos de review: **approve / request changes / comment**.
- Tres merge methods: **merge commit / squash / rebase**; sabe qué hace cada uno con la historia.
- **CODEOWNERS** asigna revisores por ruta automáticamente.
- La **branch protection** aplica sus reglas *a través* del PR (approvals, checks required).
- Contribuir a un repo ajeno: **fork → PR** (no tienes permiso de push directo).

## Conceptos clave

- **Pull Request** — propuesta de fusión con revisión y CI.
- **Head / Base** — rama origen / rama destino del PR.
- **Review** — approve / request changes / comment.
- **Merge / Squash / Rebase** — las tres estrategias de integración.
- **CODEOWNERS** — revisores automáticos por ruta.

## Siguiente

→ [04 — GitHub Projects](04-projects.md)
