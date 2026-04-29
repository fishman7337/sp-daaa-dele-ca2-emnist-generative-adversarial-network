# MLOps

## Goals

The repository now separates coursework exploration from reusable engineering assets:

- The original notebook remains available for auditability.
- Split notebooks make large sections easier to review.
- Python utilities under `src/emnist_gan` are testable without running full model training.
- CI verifies code quality, tests, split notebooks, and security checks.

## Environment Management

Use `.env.example` as the template for local configuration. Keep the real `.env` untracked.

Core development dependencies are lightweight:

```bash
python -m pip install -e ".[dev]"
```

Full notebook dependencies are optional:

```bash
python -m pip install -e ".[ml,notebook]"
```

## Data And Artifact Versioning

Keep these local-only unless a deliberate artifact release process is created:

- `data/raw/`
- `data/interim/`
- `data/processed/`
- `artifacts/models/`
- `artifacts/logs/`
- `reports/figures/`

Recommended future upgrades:

- DVC or Git LFS for controlled dataset/model versioning.
- MLflow for experiment metadata and model registry.
- Reproducible training entrypoints under `src/emnist_gan`.

## CI Controls

GitHub Actions runs:

- Ruff linting.
- Pytest with coverage.
- Split notebook verification.
- Bandit static security scanning.
- `pip-audit` dependency auditing.
- CodeQL Python analysis.

## Experiment Governance

Each meaningful experiment should record:

- Dataset version or source.
- Preprocessing settings.
- Model family and hyperparameters.
- Random seed.
- Training runtime and hardware.
- Metric outputs.
- Representative generated samples.
- Known failure modes.

## Release Checklist

Before tagging a release:

- Run all validation commands locally.
- Confirm the original notebook still opens.
- Regenerate split notebooks after notebook edits.
- Confirm no datasets, secrets, checkpoints, or logs are staged.
- Update `CHANGELOG.md`, `README.md`, and model/data documentation.
