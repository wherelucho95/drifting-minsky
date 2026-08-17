# 05 — GitHub Actions

## Situación

Cada vez que alguien abre un PR en `drifting-minsky`, quieres que **automáticamente**
se corran `pytest` y el linter. Si fallan, que el PR se marque en rojo y no se pueda
fusionar. Nadie debería tener que acordarse de correr los tests a mano. Eso es
**Integración Continua (CI)**, y en GitHub se hace con **GitHub Actions**.

## Objetivo

- Entender qué es Actions y su vocabulario: **workflow, event, job, step, action, runner**.
- Leer y escribir un workflow YAML real que corre los tests de este proyecto.
- Conocer los **triggers** (`on:`) más comunes y la relación con PRs (status checks).
- Saber qué son las **actions del Marketplace**, los **secrets** y los **runners**.
- Ubicar Actions dentro de CI/CD y del "desarrollo moderno".

## Qué es GitHub Actions

**GitHub Actions** es la plataforma de automatización de GitHub. Ejecuta flujos de
trabajo (**workflows**) en respuesta a **eventos** del repo (un push, un PR, un release,
un cron…). Su uso más común es **CI/CD** (probar y desplegar código), pero sirve para
cualquier automatización: etiquetar issues, publicar paquetes, saludar a nuevos
contribuidores, etc.

## Vocabulario (esto cae literal en el examen)

- **Workflow** — el proceso automatizado completo. Se define en un archivo YAML dentro
  de `.github/workflows/`. Un repo puede tener varios.
- **Event (trigger)** — lo que dispara el workflow: `push`, `pull_request`, `schedule`,
  `workflow_dispatch` (manual), `release`, etc. Se declara en `on:`.
- **Job** — un conjunto de steps que corren juntos en el **mismo runner**. Por defecto
  los jobs corren **en paralelo**; con `needs:` se encadenan.
- **Step** — un paso dentro de un job. Puede ser un comando de shell (`run:`) o usar una
  **action** (`uses:`).
- **Action** — una unidad reutilizable y empaquetada (ej. `actions/checkout`). Se
  comparten en el **GitHub Marketplace**.
- **Runner** — la máquina que ejecuta el job. **GitHub-hosted** (Ubuntu/Windows/macOS que
  GitHub provee y destruye tras cada corrida) o **self-hosted** (tuya).

Jerarquía: **Workflow → (uno o más) Jobs → (uno o más) Steps → cada step corre un
comando o usa una Action, todo dentro de un Runner.**

## Un workflow real para `drifting-minsky`

Este archivo vive en [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml)
(lo creamos de verdad en el repo). Léelo línea por línea:

```yaml
name: CI                        # nombre que verás en la pestaña Actions

on:                             # EVENTOS que disparan el workflow
  push:
    branches: [main]            # cada push a main
  pull_request:                 # y cada PR (aquí es donde protege main)
  workflow_dispatch:            # y un botón para lanzarlo a mano

jobs:
  test:                         # un job llamado "test"
    runs-on: ubuntu-latest      # runner hospedado por GitHub
    steps:
      - uses: actions/checkout@v4          # 1) clona tu repo en el runner
      - uses: actions/setup-python@v5      # 2) instala Python
        with:
          python-version: "3.11"
      - uses: actions/setup-java@v4        # 3) PySpark necesita una JVM
        with:
          distribution: temurin
          java-version: "17"
      - run: pip install -e ".[dev]"       # 4) instala el proyecto y pytest
      - run: pytest                         # 5) corre los tests
```

Qué está pasando:

1. `actions/checkout` — action del Marketplace que trae tu código al runner. Casi todos
   los workflows empiezan así.
2. `setup-python` / `setup-java` — actions oficiales que preparan los runtimes. PySpark
   corre sobre la JVM, por eso instalamos Java.
3. `run:` — comandos de shell normales; `pip install`, `pytest`.
4. Si `pytest` sale con código ≠ 0, el step falla → el job falla → el **check del PR se
   pone rojo**.

## Cómo se conecta con los Pull Requests

- El trigger `pull_request` hace que el workflow corra en cada PR. El resultado aparece
  como un **check** (verde si pasa, rojo si falla) en la conversación del PR
  ([tema 03](03-pull-requests.md)).
- En **branch protection** ([tema 07](07-seguridad-y-admin.md)) puedes marcar ese check
  como **required**: sin CI en verde, el botón Merge se bloquea. Así "los tests deben
  pasar" deja de ser un acuerdo verbal y pasa a ser una regla.

## Triggers (`on:`) que debes reconocer

| Evento | Cuándo dispara |
|--------|----------------|
| `push` | Al empujar commits (puedes filtrar por rama/ruta/tag) |
| `pull_request` | Al abrir/actualizar un PR |
| `workflow_dispatch` | Manual, desde la UI o `gh workflow run` |
| `schedule` | En un cron (ej. `cron: "0 6 * * 1"` = lunes 6:00 UTC) |
| `release` | Al publicar un release (útil para CD/deploy) |
| `issues`, `issue_comment` | Automatizar sobre issues |

## Matriz, secrets y variables

- **Matrix** — corre el mismo job con varias combinaciones:

  ```yaml
  strategy:
    matrix:
      python-version: ["3.11", "3.12"]
  ```

  GitHub lanza un job por cada valor (probar en varias versiones a la vez).

- **Secrets** — datos sensibles (tokens, contraseñas) guardados en
  *Settings → Secrets and variables → Actions*. Nunca en el YAML. Se leen así:

  ```yaml
  - run: ./deploy.sh
    env:
      API_TOKEN: ${{ secrets.API_TOKEN }}
  ```

- **`GITHUB_TOKEN`** — un token que GitHub crea e inyecta automáticamente en cada
  workflow para que las actions interactúen con el repo (comentar PRs, crear releases)
  sin que configures nada.

## Marketplace y actions reutilizables

El **GitHub Marketplace** aloja miles de **Actions** publicadas (y también **Apps**).
En vez de escribir todo con `run:`, reutilizas piezas probadas con `uses: owner/repo@version`.
Oficiales frecuentes: `actions/checkout`, `actions/setup-python`, `actions/cache`,
`actions/upload-artifact`. **Fija siempre una versión** (`@v4`) por seguridad y
reproducibilidad.

## Runners: hosted vs self-hosted

| | **GitHub-hosted** | **Self-hosted** |
|---|-------------------|-----------------|
| Quién la mantiene | GitHub | Tú |
| Ciclo de vida | Limpia y efímera por corrida | Persistente (tú la administras) |
| Cuándo usarla | Caso general | Hardware especial, red interna, GPUs, dependencias pesadas |
| Costo | Minutos incluidos/facturados por plan | Tu propia infra |

Los minutos de GitHub-hosted son **gratis e ilimitados en repos públicos**; en privados
hay una cuota mensual según el plan ([tema 08](08-productos-y-ecosistema.md)).

## Actions vs CI/CD vs otras herramientas

- **CI (Integración Continua)** — integrar y **probar** cambios seguido (nuestro `pytest`).
- **CD (Entrega/Despliegue Continuo)** — **desplegar** automáticamente (trigger `release`
  o push a `main` que publica). Actions hace ambas.
- Actions compite con Jenkins, GitLab CI, CircleCI… pero está **integrado nativamente**
  en el repo, que es su gran ventaja para el examen.

## En el examen (GH-900)

- Jerarquía **Workflow → Job → Step → Action**, y que corren en un **Runner**.
- Los workflows viven en **`.github/workflows/*.yml`**.
- **Event/trigger** en `on:` (`push`, `pull_request`, `schedule`, `workflow_dispatch`).
- Los jobs corren **en paralelo** salvo que uses `needs:`.
- **Runners**: GitHub-hosted (efímeros) vs self-hosted (tuyos).
- **Secrets** guardan datos sensibles; nunca van en el YAML.
- **Marketplace** = donde se publican y reutilizan Actions y Apps.
- Actions es la herramienta de **CI/CD** de GitHub (dominio "desarrollo moderno").

## Conceptos clave

- **Workflow / Job / Step / Action / Runner** — el vocabulario base de Actions.
- **Trigger (`on:`)** — el evento que dispara el workflow.
- **Marketplace** — catálogo de Actions reutilizables (`uses:`).
- **Secret** — credencial cifrada para usar en workflows.
- **Required status check** — el check de CI que bloquea el merge si falla.

## Siguiente

→ [06 — Colaboración y comunidad](06-colaboracion-comunidad.md)
