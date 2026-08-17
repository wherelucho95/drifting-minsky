# Git Playbook — Drifting Minsky

Quince escenarios secuenciales para aprender Git desde lo básico hasta `bisect`,
`worktree` y rescates con `reflog`. Cada escenario es una historia con un objetivo
concreto: nunca son comandos sueltos.

## Cómo leer un escenario

Cada archivo `NN-*.md` tiene la misma estructura:

1. **Situación** — la historia ("estás haciendo X cuando pasa Y").
2. **Objetivo** — qué te vas a llevar.
3. **Comandos paso a paso** — cada flag explicado.
4. **Qué hace el "compañero"** — cuando el escenario lo requiere, el asistente
   corre commits desde `teammate/` para forzar la situación.
5. **Verificación** — `git log --oneline --graph --all` esperado.
6. **Conceptos clave** — glosario corto.

## Convenciones del entorno

- Todo vive bajo `C:\Users\Luis\Desktop\Github\`.
- `origin.git/` es el remote (un repo `--bare`, sin working tree).
- `drifting-minsky/` es tu clon, donde tú trabajas.
- `teammate/` es el clon del "compañero" (el asistente). Tiene su propia identidad
  git local (`Ana Dev <ana@example.com>`) para que los commits se vean distintos en
  `git log`.

## Los 15 escenarios

| # | Título | Comandos clave |
|---|--------|----------------|
| [00](scenarios/00-setup.md) | Setup del entorno y `origin.git` bare | `init --bare`, `clone`, `remote -v` |
| [01](scenarios/01-first-commit-push.md) | Primer commit y push a `main` | `add`, `commit`, `push -u origin main`, `log` |
| [02](scenarios/02-feature-branch.md) | Feature branch | `switch -c`, `push`, `diff` |
| [03](scenarios/03-main-avanzo-fetch-rebase.md) | **Main avanzó mientras estabas en tu rama** | `fetch`, `log A..B`, `rebase`, `push --force-with-lease` |
| [04](scenarios/04-merge-vs-rebase.md) | Merge vs rebase | `merge --no-ff`, `rebase` |
| [05](scenarios/05-conflict-resolution.md) | Conflictos reales | edición de markers, `add`, `rebase --continue`, `--abort` |
| [06](scenarios/06-stash.md) | Stash a mitad de trabajo | `stash push -m`, `pop`, `list`, `drop` |
| [07](scenarios/07-cherry-pick.md) | Cherry-pick un fix de main | `cherry-pick <sha>` |
| [08](scenarios/08-amend-y-rebase-interactivo.md) | Limpiar historia antes del PR | `commit --amend`, `rebase -i` |
| [09](scenarios/09-reset-vs-revert.md) | Reset vs revert | `reset --soft/--mixed/--hard`, `revert` |
| [10](scenarios/10-reflog-rescate.md) | Rescate con reflog | `reflog`, `branch <nombre> <sha>` |
| [11](scenarios/11-bisect.md) | Encontrar el commit malo | `bisect start/good/bad/reset` |
| [12](scenarios/12-tags-y-release.md) | Tags y releases | `tag -a`, `push --tags`, `describe` |
| [13](scenarios/13-worktree.md) | Dos ramas a la vez sin stash | `worktree add/list/remove` |
| [14](scenarios/14-migracion-a-github.md) | Migrar el remote a GitHub real | `gh repo create`, `remote set-url`, PR |

## Glosario express

- **Working tree** — los archivos tal como están en tu carpeta ahora mismo.
- **Staging area / index** — la "antesala" del próximo commit (lo que pones con `git add`).
- **HEAD** — puntero a tu commit actual (normalmente el último de tu rama).
- **Rama** — un nombre que apunta a un commit. No es una carpeta ni una copia.
- **Remote** — otro repo (puede ser local o en internet). `origin` es el nombre por convención.
- **Fast-forward** — cuando una rama puede avanzar sin crear un merge commit (línea recta).
- **Merge commit** — commit con dos padres, fusiona dos historias.
- **Rebase** — reescribe tus commits encima de otra base. Cambia los SHA.
- **Detached HEAD** — estás parado en un commit que no es la punta de ninguna rama.
- **Conflicto** — Git no puede decidir cómo combinar dos cambios; te pide ayuda.

## Reglas de oro

1. **Nunca hagas `--force` a una rama compartida**. Usa `--force-with-lease`, que aborta si alguien hizo push después de ti.
2. **No reescribas historia que ya está pusheada y otros usan**. Rebase es para tu rama personal antes del PR.
3. **`git status` antes y después de cada operación.** Es el comando más barato y más útil.
4. **`git log --oneline --graph --all --decorate`** es tu mapa: úsalo para entender qué pasó.
5. **`git reflog`** es tu red de seguridad: casi nada se borra realmente en 90 días.
