# 01 — Crear el proyecto en GitHub (repositorios)

## Situación

En el [git-playbook](../git-playbook.md) todo vivía en local: un `origin.git` bare
en tu disco. Eso está bien para aprender Git, pero un equipo real necesita un repo
**en GitHub**: con URL pública, control de acceso, issues y CI. En este tema publicas
`drifting-minsky` en github.com y aprendes todo lo que el examen pregunta sobre repos.

## Objetivo

- Saber qué **es** un repositorio de GitHub y qué lo diferencia de una carpeta con Git.
- Crear un repo por la web y con `gh` (GitHub CLI).
- Entender **visibilidad** (public / private / internal) y los archivos "de higiene":
  README, LICENSE, `.gitignore`.
- Distinguir **clone** vs **fork**, y **HTTPS** vs **SSH**.
- Manejar Markdown de GitHub, releases y la anatomía de la página del repo.

## Qué es un repositorio en GitHub

Un repo de GitHub = el repositorio Git (código + historial) **más** una capa social y
de gestión que Git no tiene: Issues, Pull Requests, Projects, Actions, Wiki, Settings,
permisos, releases. Es la unidad básica de trabajo en la plataforma.

Anatomía de la página de un repo (las pestañas que caen en el examen):

- **Code** — archivos, ramas, commits, releases, tags.
- **Issues** — tareas, bugs, ideas → [tema 02](02-issues.md).
- **Pull requests** — cambios propuestos → [tema 03](03-pull-requests.md).
- **Actions** — automatización/CI → [tema 05](05-actions.md).
- **Projects** — tableros de planificación → [tema 04](04-projects.md).
- **Wiki** — documentación larga → [tema 06](06-colaboracion-comunidad.md).
- **Security** — políticas y alertas → [tema 07](07-seguridad-y-admin.md).
- **Insights** — gráficos de actividad, contributors, dependency graph.
- **Settings** — configuración (solo con permiso de admin).

## Camino A — Crear el repo desde la web

1. Arriba a la derecha: **+** → **New repository**.
2. **Owner**: tu cuenta o una organización.
3. **Repository name**: `drifting-minsky`.
4. **Description**: "Pipeline ETL de e-commerce con PySpark para practicar Git y GitHub".
5. **Visibility**:
   - **Public** — cualquiera lo ve. No significa que cualquiera pueda escribir: para
     eso hace falta permiso. (Distinción muy preguntada.)
   - **Private** — solo tú y quienes invites.
   - **Internal** — solo miembros de tu organización/empresa (existe en GitHub
     Enterprise). Base de la práctica **InnerSource**.
6. **Initialize**: puedes añadir **README**, **.gitignore** (plantilla Python) y **LICENSE**.
   > Si el repo **ya existe en local** (como el nuestro), NO inicialices con README:
   > crearías un commit que choca con tu historia. Créalo vacío y sube lo que ya tienes.

## Camino B — Crear el repo con `gh` (GitHub CLI)

`gh` es la línea de comandos oficial de GitHub. Autentícate una vez:

```bash
gh auth login              # elige GitHub.com → HTTPS → autenticar por navegador
gh auth status             # verifica que quedaste logueado
```

Como nuestro `drifting-minsky/` ya tiene commits (los del git-playbook), lo publicamos
así:

```bash
cd /c/Users/Luis/Desktop/Github/drifting-minsky
gh repo create drifting-minsky --public --source=. --remote=origin --push
```

- `--source=.` usa el repo local actual.
- `--remote=origin` nombra el nuevo remote de GitHub como `origin` (o `github` si ya
  usas `origin` para el bare local — puedes tener varios remotes).
- `--push` empuja `main` de una vez.

Verifica:

```bash
git remote -v              # debe aparecer la URL https://github.com/<user>/drifting-minsky.git
gh repo view --web         # abre el repo en el navegador
```

> Esto es exactamente lo que el **escenario 14** del git-playbook ("Migrar el remote
> a GitHub real") formaliza. Aquí lo ves desde la óptica de la plataforma.

## Los tres archivos de higiene de un repo

El examen los agrupa como "community/health files". Los básicos:

- **README.md** — la portada. GitHub lo renderiza automáticamente en la página del repo.
  Debe decir: qué es, cómo instalar, cómo usar. El nuestro ya existe.
- **LICENSE** — define qué pueden hacer otros con tu código. **Sin licencia, un repo
  público sigue teniendo todos los derechos reservados**: verlo no da derecho a usarlo.
  Licencias típicas: MIT y Apache-2.0 (permisivas), GPL (copyleft: obliga a compartir
  derivados con la misma licencia).
- **.gitignore** — qué NO versionar. El nuestro ya ignora `__pycache__/`, `.venv/`,
  CSVs de `data/raw/`, artefactos de Spark, etc.

Otros health files que GitHub reconoce (y pregunta):

- `CONTRIBUTING.md` — cómo contribuir.
- `CODE_OF_CONDUCT.md` — normas de convivencia.
- `SECURITY.md` — cómo reportar vulnerabilidades → [tema 07](07-seguridad-y-admin.md).
- `CODEOWNERS` — quién revisa qué rutas → [tema 03](03-pull-requests.md).
- Plantillas de issues y PR → [tema 02](02-issues.md).

Un archivo `README.md` dentro de una carpeta especial `.github/` o en un repo con tu
mismo nombre de usuario aparece como **perfil**; no es examinable a fondo, pero suele
mencionarse.

## Clone vs Fork — la comparación estrella

| | **Clone** | **Fork** |
|---|-----------|----------|
| Qué hace | Copia el repo a tu **máquina** | Copia el repo a **tu cuenta** de GitHub |
| Dónde queda | Local | En GitHub, bajo tu usuario |
| Para qué | Trabajar en un repo al que ya tienes acceso | Contribuir a un repo **ajeno** sin permiso de escritura |
| Comando | `git clone <url>` | Botón **Fork** (o `gh repo fork`) |

Flujo típico de contribución open source (cae seguro): **Fork** el repo ajeno →
**clone** tu fork → creas rama → commit → push a tu fork → abres un **Pull Request**
hacia el repo original. Ver [tema 03](03-pull-requests.md).

## HTTPS vs SSH (cómo clonas)

```bash
git clone https://github.com/usuario/drifting-minsky.git   # HTTPS: pide token/credenciales
git clone git@github.com:usuario/drifting-minsky.git       # SSH: usa tu par de claves
```

- **HTTPS** — más simple; se autentica con un **Personal Access Token (PAT)**, no con
  tu contraseña (GitHub removió el password para Git desde 2021).
- **SSH** — subes tu clave pública una vez a *Settings → SSH keys* y ya no metes credenciales.

## Markdown de GitHub (GFM)

GitHub renderiza **GitHub Flavored Markdown** en READMEs, issues, PRs y comentarios.
Lo mínimo que cae:

```markdown
# Título   ## Subtítulo
**negrita**   *itálica*   `código en línea`
- lista        1. lista ordenada
- [ ] tarea pendiente   - [x] tarea hecha   ← "task list"
[texto](https://url)    ![imagen](ruta.png)
> cita
| col A | col B |   ← tablas
```code block```        @usuario  #123 (referencia a issue/PR)  :rocket: (emoji)
```

Las **task lists** (`- [ ]`) en un issue muestran una barra de progreso: clave para
gestión de proyectos ([tema 04](04-projects.md)).

## Releases y tags

- Un **tag** de Git (`git tag v1.0.0`) marca un commit. GitHub lo puede envolver en un
  **Release**: página con notas, changelog y binarios adjuntos descargables.
- En la web: pestaña **Releases** → **Draft a new release** → eliges un tag, escribes
  notas (GitHub puede **autogenerarlas** desde los PRs) y publicas.
- El escenario 12 del git-playbook cubre `git tag`; el Release es la capa GitHub encima.

## En el examen (GH-900)

- **Public ≠ cualquiera puede escribir.** Público = visible; escribir requiere permiso.
- **Internal** = visible solo dentro de la organización (Enterprise) → base de InnerSource.
- **Sin LICENSE**, "todos los derechos reservados" aunque el repo sea público.
- **Fork** = copia en TU cuenta de GitHub; **clone** = copia en TU máquina.
- El **README** se renderiza solo en la portada del repo.
- Reconoce los health files (`CONTRIBUTING`, `CODE_OF_CONDUCT`, `SECURITY`, `CODEOWNERS`).
- GitHub usa **GitHub Flavored Markdown**; sabe reconocer task lists y referencias `#123`.

## Conceptos clave

- **Repository** — código + historial + capa social/gestión de GitHub.
- **Visibilidad** — public / private / internal.
- **Fork / Clone** — copia en tu cuenta vs copia en tu máquina.
- **PAT** — Personal Access Token, reemplaza la contraseña para Git sobre HTTPS.
- **Release** — página publicable construida sobre un tag de Git.

## Siguiente

→ [02 — Issues](02-issues.md)
