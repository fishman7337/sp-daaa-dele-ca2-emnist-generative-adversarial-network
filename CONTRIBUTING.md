# Contributing

Thank you for improving the EMNIST Generative Modeling Lab. Keep changes focused, reproducible, and respectful of the original coursework notebook.

## Development Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Install optional ML dependencies only when running the notebook or model builders:

```bash
python -m pip install -e ".[ml,notebook]"
```

## Contribution Flow

1. Create a focused branch from `main`.
2. Keep datasets, checkpoints, logs, and `.env` files out of git.
3. Add or update tests for reusable Python changes.
4. Update docs when changing project structure, commands, or experiment assumptions.
5. Run the validation commands below before opening a pull request.

## Validation

```bash
ruff check .
pytest
python scripts/split_notebook.py --source "DELE_CA2_A (8).ipynb" --output notebooks/parts --check
bandit -q -r src scripts
pip-audit -r requirements.txt -r requirements-dev.txt
```

## Notebook Changes

The original notebook should remain available for auditability. If it changes, regenerate the split notebooks:

```bash
python scripts/split_notebook.py --source "DELE_CA2_A (8).ipynb" --output notebooks/parts
```

Generated split notebooks should remain source-only with outputs removed.
