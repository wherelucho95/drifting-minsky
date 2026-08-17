# Escenario 03 — Main avanzó mientras estabas en tu rama

## Situación (la que pediste explícitamente)

Llevas dos horas en tu feature branch `feature/ingest-orders`. Ya hiciste un commit
con `ingest.py` y la pusheaste. Justo cuando ibas a abrir el PR, recibes un Slack:

> **Ana Dev**: subí dos commits a main, uno cambia el `.gitignore` y otro arregla
> el `README`. ¡Aviso!

Tu rama ahora está **adelantada** en lo tuyo y **desactualizada** respecto a `main`.
Si abres el PR así, GitHub te dirá "this branch is out of date with the base branch".

¿Qué haces?

## Objetivo

- Diferenciar `git fetch` de `git pull` (saber qué hace cada uno y por qué importa).
- Inspeccionar qué hay en el remote sin mezclar nada todavía.
- Decidir entre **rebase** y **merge** para sincronizar.
- Hacer un `push --force-with-lease` cuando reescribes tu rama tras rebase.

## Lo que hará el "compañero" (asistente)

Antes de que tú empieces el escenario, el asistente irá a `teammate/`, hará dos
commits en `main` y los pusheará. Son cambios que NO tocan los mismos archivos
que tú, así que no habrá conflicto todavía (los conflictos llegan en el escenario 05).

Commits que aparecerán en `origin/main`:
1. `chore: ampliar .gitignore con archivos de Spark` (modifica `.gitignore`)
2. `docs: corregir typo en README` (modifica `README.md`)

## Comandos paso a paso

### 1. Verifica tu situación local primero

```bash
cd /c/Users/Luis/Desktop/Github/drifting-minsky
git status                           # working tree clean
git branch -vv                       # ve dónde está tu rama vs origin
```

### 2. `git fetch` — descargar SIN integrar

```bash
git fetch origin
```

Esto descarga los commits nuevos de `origin/main` a tu repo local, pero **NO los
mezcla con tu rama**. La diferencia clave con `git pull`:

| Comando | Descarga | Integra |
|---------|----------|---------|
| `git fetch` | Sí | No |
| `git pull` | Sí | Sí (con merge o rebase según config) |

**Regla práctica**: cuando no sabes qué hay del otro lado, siempre `fetch` primero
y mira con `log` antes de integrar.

### 3. Ver qué cambió

```bash
git status
# Tu rama feature/ingest-orders sigue donde la dejaste, pero origin/main avanzó.

git log --oneline --graph --all --decorate -10
# Verás algo como:
#   * <sha_C> (origin/main) docs: corregir typo en README       <- de Ana
#   * <sha_B> chore: ampliar .gitignore con archivos de Spark   <- de Ana
#   | * <sha_A> (HEAD -> feature/ingest-orders, origin/feature/ingest-orders) feat(ingest): ...
#   |/
#   * <sha_0> docs: nota de prueba en README
#   * <sha_init> chore: initial scaffolding
```

```bash
# ¿Qué commits tiene origin/main que mi rama NO tiene?
git log feature/ingest-orders..origin/main --oneline
# Muestra los 2 commits de Ana

# ¿Qué commits tengo yo que origin/main NO tiene?
git log origin/main..feature/ingest-orders --oneline
# Muestra tu commit feat(ingest)

# Doble punto = "lo que está en B y no en A". El orden importa.
```

### 4. Decisión: ¿merge o rebase?

```
Estado actual:
                    A (tu commit)
                   /
  ---0---X---B---C (origin/main avanzó)
```

**Opción a) Merge de `origin/main` en tu rama**:
```
                    A----M (merge commit)
                   /    /
  ---0---X---B---C-----
```
Crea un merge commit en TU rama. Pros: no reescribe historia. Contras: ensucia tu
rama con un merge solo para sincronizar.

**Opción b) Rebase de tu rama sobre `origin/main`**:
```
                          A' (mismo cambio, nuevo SHA)
                         /
  ---0---X---B---C-------
```
Mueve tu commit `A` a estar después de `C`, dándole nuevo SHA (`A'`). Pros: historia
lineal y limpia. Contras: reescribe SHAs, hay que hacer `push --force-with-lease`.

**Convención de equipo común**: rebase tu rama personal antes del PR. Merge para
integrar el PR a `main`.

### 5. Hacer el rebase

```bash
git switch feature/ingest-orders     # asegúrate de estar en tu rama
git rebase origin/main
```

Resultado esperado (sin conflictos, porque Ana tocó archivos distintos):
```
Successfully rebased and updated refs/heads/feature/ingest-orders.
```

### 6. Inspeccionar el resultado

```bash
git log --oneline --graph --all --decorate -10
# Tu commit ahora aparece DESPUÉS de los de Ana:
#   * <sha_A'> (HEAD -> feature/ingest-orders) feat(ingest): ...
#   * <sha_C>  (origin/main) docs: corregir typo en README
#   * <sha_B>  chore: ampliar .gitignore con archivos de Spark
#   * <sha_0>  docs: nota de prueba en README
```

Tu commit `A` cambió de SHA: ahora es `A'`. Es el "mismo cambio" lógicamente, pero
un commit nuevo. Esto importa mucho.

### 7. Push con `--force-with-lease`

Tu rama remota `origin/feature/ingest-orders` todavía apunta al SHA viejo (`A`).
Tu rama local ahora tiene `A'`. Git no te dejará pushear normal:

```bash
git push
# error: failed to push some refs ... Updates were rejected because the tip of
# your current branch is behind ...
```

La solución es forzar el push, pero NUNCA con `--force` a secas. Usa la versión
segura:

```bash
git push --force-with-lease
```

**`--force-with-lease`** = "fuerza el push, PERO solo si la rama remota está
exactamente donde yo creo que está". Si alguien (no Ana, sino otro tú futuro o
otro compañero) pusheó a tu rama entre medias, el comando aborta. Es la red de
seguridad.

**`--force`** a secas pisa todo sin chequear. Tabú en ramas compartidas.

### 8. Verificación final

```bash
git status                           # up to date with origin
git log --oneline --graph --all -10
git branch -vv                       # tu rama y su upstream sincronizados
```

## ¿Y si hubiera elegido merge en vez de rebase?

```bash
git switch feature/ingest-orders
git merge origin/main
# Crea un merge commit "Merge branch 'main' into feature/ingest-orders"
git push                             # SIN force-with-lease, porque no reescribiste nada
```

Funciona, pero deja un merge commit en tu rama que muchos equipos consideran ruido.

## Variantes útiles del comando

```bash
git pull --rebase                    # fetch + rebase en un comando
git pull --ff-only                   # solo permite avanzar si es fast-forward (seguro)
git config pull.rebase true          # por defecto, pull = pull --rebase
```

## Verificación

```bash
git log --oneline --graph --all --decorate
# Línea recta sin merge commit en tu rama:
#   * (HEAD -> feature/ingest-orders, origin/feature/ingest-orders) feat(ingest): ...
#   * (origin/main, main) docs: corregir typo en README
#   * chore: ampliar .gitignore con archivos de Spark
#   * docs: nota de prueba en README
#   * chore: initial scaffolding
```

## Conceptos clave

- **`fetch` ≠ `pull`**: fetch descarga, pull descarga e integra. Siempre fetch primero cuando dudas.
- **`A..B`** en `git log`: commits que están en `B` y no en `A`.
- **Rebase reescribe SHAs**: lo que antes era `abc1234` ahora es `def5678`. Por eso necesitas force-push.
- **`--force-with-lease`**: force-push seguro. La única forma aceptable de force-push.
- **No rebases ramas compartidas**: si tu rama es solo tuya, rebase OK. Si otros la usan, te van a odiar.

## Siguiente

→ [04 — Merge vs rebase](04-merge-vs-rebase.md) (comparación profunda con ejemplo guiado)
