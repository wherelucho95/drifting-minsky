# Escenario 00 — Setup: crear el `origin.git` bare y los dos clones

## Situación

Acabas de unirte al equipo. No hay GitHub aún — la empresa usa un servidor interno.
Para simularlo en local: vamos a crear un **repo bare** (`origin.git`) que actúa
como el servidor remoto, y luego clonarlo dos veces:

- `drifting-minsky/` — tu clon principal de trabajo.
- `teammate/` — el clon de tu "compañera" Ana Dev (lo manejará el asistente).

## Objetivo

- Entender qué es un repo bare y por qué los remotes siempre son bare.
- Practicar `git init --bare`, `git clone`, `git remote -v`, `git config` local.

## Estado de partida

```
C:\Users\Luis\Desktop\Github\
└── drifting-minsky/   ← carpeta con archivos pero SIN git inicializado todavía
```

## Comandos paso a paso

> **Importante**: el proyecto `drifting-minsky/` ya tiene archivos (el scaffolding
> que armamos). Vamos a inicializar git ahí y publicarlo en `origin.git`.

### 1. Crear el `origin.git` bare

```bash
cd /c/Users/Luis/Desktop/Github
git init --bare origin.git
```

- `--bare` significa "sin working tree": no hay archivos para editar, solo la base
  de datos de git. Los servidores remotos siempre son bare. Verás que dentro hay
  `HEAD`, `config`, `objects/`, `refs/`, etc., pero ningún `.py`.

### 2. Inicializar git en tu proyecto y hacer el primer commit

```bash
cd /c/Users/Luis/Desktop/Github/drifting-minsky
git init -b main
git status                       # ve qué archivos detecta (untracked)
git add .
git status                       # ahora todo aparece como "Changes to be committed"
git commit -m "chore: initial scaffolding"
```

- `init -b main` crea el repo con la rama por defecto llamada `main` (antes era `master`).
- `git add .` agrega TODO lo que no esté ignorado por `.gitignore`.
- El `.gitignore` ya excluye `data/raw/*.csv`, `__pycache__/`, `.venv/`, etc.

### 3. Conectar tu clon con el `origin.git` bare

```bash
git remote add origin /c/Users/Luis/Desktop/Github/origin.git
git remote -v                    # debe listar origin (fetch) y origin (push)
git push -u origin main
```

- `remote add origin <url>` registra el remote. La URL aquí es una ruta local.
- `-u` (= `--set-upstream`) hace que `git push` y `git pull` futuros sepan a dónde
  ir sin parámetros.

### 4. (Lo hará el asistente) Clonar `teammate/`

Esto lo correrá el asistente para simular a la compañera:

```bash
cd /c/Users/Luis/Desktop/Github
git clone origin.git teammate
cd teammate
git config user.name "Ana Dev"
git config user.email "ana.dev@example.com"
```

- `git config` sin `--global` solo afecta a ESE repo. Así los commits que hagas en
  `drifting-minsky/` siguen siendo tuyos, y los que se hagan en `teammate/` van
  como "Ana Dev".

## Verificación

```bash
cd /c/Users/Luis/Desktop/Github/drifting-minsky
git log --oneline --graph --all --decorate
```

Esperado:
```
* <sha> (HEAD -> main, origin/main) chore: initial scaffolding
```

Y:
```bash
ls /c/Users/Luis/Desktop/Github
# debe mostrar: drifting-minsky/  origin.git/  teammate/   (teammate aparece tras el paso 4)
```

## Conceptos clave

- **Bare repo**: repo sin working tree. Es lo que vive en un servidor.
- **Remote**: puntero a otro repo, con un alias (`origin` por convención).
- **Upstream**: la rama del remote a la que tu rama local está "casada" (`-u`).
- **Identidad git local**: `git config user.name` sin `--global` solo aplica a ese repo.

## Siguiente

→ [01 — Primer commit y push a `main`](01-first-commit-push.md) (lo hiciste en el paso 2 y 3; el siguiente archivo lo formaliza y agrega comandos de inspección).
