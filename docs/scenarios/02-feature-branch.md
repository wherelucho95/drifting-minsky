# Escenario 02 — Feature branch para agregar `ingest.py`

## Situación

Tu equipo usa el flujo **trunk-based con feature branches cortas**:
1. Salir de `main` con una rama nueva por cada feature.
2. Trabajar, commitear, pushear esa rama.
3. Abrir un PR a `main` cuando esté lista.

Tu primera tarea: agregar `src/drifting_minsky/pipelines/ingest.py` con la
función `read_orders()` que lee `data/raw/orders.csv` en un DataFrame.

## Objetivo

- Crear y moverse entre ramas con `switch` (la sintaxis moderna).
- Entender la diferencia entre `git branch` (gestión) y `git switch` (moverse).
- Pushear una rama nueva y entender el upstream.

## Comandos paso a paso

### 1. Asegúrate de partir de `main` actualizado

```bash
cd /c/Users/Luis/Desktop/Github/drifting-minsky
git switch main
git status                           # working tree clean
git pull                             # nada nuevo aún, pero acostúmbrate
```

### 2. Crear la rama feature

```bash
git switch -c feature/ingest-orders
# equivalente antiguo: git checkout -b feature/ingest-orders
```

- `-c` crea la rama y se cambia a ella en un solo paso.
- Nombre `feature/ingest-orders` es convención (puedes usar `feat/`, `lcastro/ingest`, etc.).

### 3. Escribir el código

Crea `src/drifting_minsky/pipelines/ingest.py` con este contenido (cópialo a mano,
es parte del aprendizaje):

```python
"""Lectura de CSVs crudos en DataFrames de Spark."""
from __future__ import annotations

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import (
    StructType, StructField, IntegerType, StringType, DateType,
)

ORDERS_SCHEMA = StructType([
    StructField("order_id", IntegerType(), nullable=False),
    StructField("customer_id", IntegerType(), nullable=False),
    StructField("product_id", IntegerType(), nullable=False),
    StructField("quantity", IntegerType(), nullable=True),
    StructField("order_date", DateType(), nullable=True),
    StructField("status", StringType(), nullable=True),
])


def read_orders(spark: SparkSession, path: str = "data/raw/orders.csv") -> DataFrame:
    return (
        spark.read
        .option("header", True)
        .schema(ORDERS_SCHEMA)
        .csv(path)
    )
```

### 4. Inspeccionar y commitear

```bash
git status                           # untracked: ingest.py
git diff                             # vacío para untracked; usa --cached después
git add src/drifting_minsky/pipelines/ingest.py
git status                           # ahora "to be committed"
git diff --staged                    # ve el código que estás por commitear
git commit -m "feat(ingest): leer orders.csv con schema explícito"
```

### 5. Push de la rama nueva

```bash
git push -u origin feature/ingest-orders
```

- `-u` registra el upstream. Sin él, `git push` solo no sabría a dónde mandar
  una rama nueva.
- En GitHub esto crearía el botón para abrir el PR. Como nuestro `origin` es bare
  local, solo aparecerá como una rama remota más.

### 6. Verificar las ramas

```bash
git branch                           # ramas locales (la actual con *)
git branch -r                        # ramas remotas (origin/main, origin/feature/ingest-orders)
git branch -a                        # todas
git log --oneline --graph --all --decorate
```

Esperado:
```
* <sha> (HEAD -> feature/ingest-orders, origin/feature/ingest-orders) feat(ingest): ...
* <sha> (origin/main, main) docs: ...
* <sha> chore: initial scaffolding
```

## `git branch` vs `git switch` vs `git checkout`

- **`git branch`** — gestiona ramas (lista, crea, borra). NO te mueve.
  - `git branch` — lista locales.
  - `git branch <nombre>` — crea sin moverse.
  - `git branch -d <nombre>` — borra (si está mergeada).
  - `git branch -D <nombre>` — fuerza borrado.
- **`git switch`** — moverse entre ramas. Sintaxis nueva (>2.23).
  - `git switch <nombre>` — moverse.
  - `git switch -c <nombre>` — crear y moverse.
- **`git checkout`** — el comando viejo que hacía las dos cosas. Sigue funcionando
  pero `switch` es más claro.

## Verificación

```bash
git log --oneline --graph --all
# Las dos ramas deben aparecer
git branch -vv
# main         <sha> [origin/main] docs: ...
# feature/ingest-orders <sha> [origin/feature/ingest-orders] feat(ingest): ...
```

## Conceptos clave

- **Rama** = puntero a un commit, nada más.
- **`-u` / `--set-upstream`**: vincula tu rama local con la remota.
- **`git branch -vv`**: muestra el upstream de cada rama, útil para auditar.

## Siguiente

→ [03 — Main avanzó mientras estabas en tu rama](03-main-avanzo-fetch-rebase.md) — el escenario que pediste.
