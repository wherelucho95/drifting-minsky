# Escenario 01 — Anatomía del primer commit y push

## Situación

Ya inicializaste el repo y empujaste a `origin` en el escenario 00. Este escenario
formaliza qué pasó por dentro y te enseña los comandos de inspección que vas a
usar todos los días.

## Objetivo

- Entender las tres áreas: working tree, staging area, repo.
- Dominar `git status`, `git diff`, `git log` y sus variantes.
- Saber leer un identificador de commit (SHA) y referirte a él.

## Las tres áreas

```
[working tree]  --git add-->  [staging area]  --git commit-->  [repo .git]
   tus archivos                  "lo próximo                       historia
   ahora mismo                    a commitear"                     inmutable
```

`git status` te dice qué hay en cada área.

## Ejercicios de inspección

Cambia algo trivial (por ejemplo, edita una línea del README) y corre estos
comandos uno por uno. Lee la salida con calma:

```bash
# 1. Modifica el README (agrega una línea cualquiera)
echo "" >> README.md
echo "<!-- nota: añadido durante el escenario 01 -->" >> README.md

# 2. Ver el estado
git status                          # debe mostrar README.md modified
git status -s                       # versión corta (M README.md)

# 3. Ver el diff sin staging
git diff                            # cambios en working tree vs último commit
git diff README.md                  # solo ese archivo

# 4. Mover al staging y volver a ver
git add README.md
git status                          # ahora aparece en "Changes to be committed"
git diff                            # ¡vacío! Porque ya no hay cambios sin stagear
git diff --staged                   # diff de lo que está EN staging vs último commit

# 5. Commit
git commit -m "docs: nota de prueba en README"

# 6. Inspeccionar la historia
git log                             # historial completo
git log --oneline                   # una línea por commit
git log --oneline --graph --all --decorate    # tu nuevo amigo: úsalo siempre
git log -1                          # solo el último commit
git log -p -1                       # último commit con su diff
git show HEAD                       # commit en HEAD con diff (equivalente)
git show HEAD~1                     # el commit anterior

# 7. Push al remote
git push                            # ya configuraste -u, no hace falta más
```

## Anatomía de un SHA

Un commit se identifica con un SHA-1 de 40 caracteres. Casi siempre basta con
los primeros 7-8:

```
git show a3f8b9c              # funciona
git show a3f8b9c2             # también
git log a3f8b9c..HEAD         # rango: desde ese commit (exclusivo) hasta HEAD
```

Además de SHAs, puedes referirte a commits con:

- `HEAD` — commit actual.
- `HEAD~1`, `HEAD~2`... — uno, dos commits atrás (siguiendo el primer padre).
- `HEAD^` — equivalente a `HEAD~1`.
- `main`, `origin/main`, `feature/x` — la punta de esa rama.
- `@{u}` — el upstream de la rama actual (típicamente `origin/main`).

## Verificación

```bash
git log --oneline
# Debe haber 2 commits:
#   <sha2> docs: nota de prueba en README
#   <sha1> chore: initial scaffolding

git status
# nothing to commit, working tree clean
```

## Conceptos clave

- **SHA**: el hash que identifica un commit. Inmutable.
- **HEAD**: puntero al commit donde estás parado.
- **`~` vs `^`**: ambos retroceden, pero `^N` selecciona el N-ésimo padre (relevante en merges, donde un commit tiene dos padres).
- **`origin/main`** ≠ **`main`**: el primero es la "última versión que vi del remote"; el segundo es tu rama local. Pueden estar desalineados.

## Siguiente

→ [02 — Feature branch para agregar `ingest.py`](02-feature-branch.md)
