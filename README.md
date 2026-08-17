# drifting-minsky

Mini-pipeline ETL de e-commerce con PySpark. Sirve como excusa para practicar Git
en escenarios realistas de trabajo en equipo.

## Qué hay aquí

- **PySpark** desde lo básico (read/clean/transform/aggregate) sobre un dataset
  sintético de e-commerce (clientes, productos, pedidos, devoluciones).
- **Git Playbook** en [`docs/git-playbook.md`](docs/git-playbook.md) — 15 escenarios
  secuenciales con comandos paso a paso, desde el primer commit hasta `bisect` y
  `worktree`.
- **GitHub Foundations (GH-900)** en
  [`docs/github-foundations.md`](docs/github-foundations.md) — guía de estudio para la
  certificación oficial: repos, issues, pull requests, projects, actions, seguridad y
  comunidad. 9 temas + un simulacro con 30 preguntas.

## Setup rápido

```bash
pip install -r requirements.txt
python -m drifting_minsky.generate_data        # genera CSVs en data/raw/
python -m drifting_minsky.pipelines.aggregate  # produce parquets en data/processed/
pytest                                          # corre los tests
```

## Estructura

```
src/drifting_minsky/
  utils/spark.py       # helper get_spark()
  generate_data.py     # generador sintético
  pipelines/
    ingest.py
    clean.py
    transform.py
    aggregate.py
tests/                 # pytest
docs/scenarios/        # 15 escenarios git con comandos
docs/github/           # 9 temas GitHub Foundations (GH-900) + simulacro
.github/workflows/     # ci.yml — Action que corre pytest en cada PR
```

## Cómo se simula el equipo

Dos clones locales apuntan a un repo bare `origin.git` (sin internet, sin cuentas):

- `drifting-minsky/` — tú
- `teammate/` — el "compañero" (identidad git distinta a nivel local del repo)

Más adelante (escenario 14) migramos el remote a GitHub real con `gh`.
