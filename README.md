# EMNIST Generative Modeling Lab

[![CI](https://github.com/fishman7337/emnist-generative-adversarial-network/actions/workflows/ci.yml/badge.svg)](https://github.com/fishman7337/emnist-generative-adversarial-network/actions/workflows/ci.yml)
[![CodeQL](https://github.com/fishman7337/emnist-generative-adversarial-network/actions/workflows/codeql.yml/badge.svg)](https://github.com/fishman7337/emnist-generative-adversarial-network/actions/workflows/codeql.yml)

Reusable documentation, notebook splits, tests, and MLOps scaffolding for an EMNIST generative modeling coursework project. The original project notebook is preserved at [`notebooks/DELE_CA2_A (8).ipynb`](notebooks/DELE_CA2_A%20(8).ipynb); smaller source-only notebook sections are generated under [`notebooks/parts`](notebooks/parts).

## Academic Context

This project was completed under Singapore Polytechnic, School of Computing, Diploma in Applied AI & Analytics, for ST1504 Deep Learning CA2 Part A. It was done by Goh Kun Ming, DAAA student, in AY25/26 Year 2 Semester 1, under Lecturer Gerald Chua Deng Xiang.

## Project Scope

The coursework explores generative modeling for selected EMNIST letter classes. The notebook covers:

- EMNIST loading, filtering, preprocessing, orientation correction, relabeling, and augmentation.
- Exploratory visual analysis including class distribution, class heatmaps, pixel variance, intensity curves, and t-SNE.
- VAE/CVAE data balancing and comparison work.
- Multiple GAN variants, including Vanilla GAN, DCGAN, WGAN, WGAN-GP, LSGAN, DRAGAN, InfoGAN, SAGAN, and cDRAGAN.
- Qualitative generated-sample review and quantitative metrics such as FID, KID, diversity, mode-collapse checks, and PPL.

## Repository Layout

```text
.
├── notebooks/
│   ├── DELE_CA2_A (8).ipynb    # Preserved original notebook
│   └── parts/                  # Generated source-only notebook sections
├── src/emnist_gan/             # Reusable Python utilities
├── tests/                      # Pytest coverage for extracted utilities
├── docs/                       # Project, data, model, and MLOps documentation
├── data/                       # Local-only dataset staging folders
├── artifacts/                  # Local-only trained model/log outputs
├── reports/figures/            # Local-only exported plots
├── scripts/                    # Automation helpers
└── .github/workflows/          # CI, security, and CodeQL workflows
```

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pytest
```

For full notebook execution with TensorFlow and visualization dependencies:

```bash
python -m pip install -e ".[ml,notebook]"
jupyter lab
```

Copy `.env.example` to `.env` for local paths and experiment defaults. Do not commit `.env`, datasets, model checkpoints, or generated logs.

## Notebook Workflow

The original notebook is intentionally retained for auditability. To regenerate the smaller notebooks:

```bash
python scripts/split_notebook.py --source "notebooks/DELE_CA2_A (8).ipynb" --output notebooks/parts
```

Generated split notebooks preserve markdown and code cell source, but remove execution counts and outputs so they stay reviewable in pull requests.

## Quality And Security

CI runs:

- `ruff check .`
- `pytest --cov=emnist_gan`
- notebook split verification
- `bandit -q -r src scripts`
- `pip-audit -r requirements.txt -r requirements-dev.txt`
- CodeQL Python analysis

Run the same checks locally before pushing:

```bash
ruff check .
pytest
bandit -q -r src scripts
pip-audit -r requirements.txt -r requirements-dev.txt
```

## Documentation

- [`docs/PROJECT_CONTEXT.md`](docs/PROJECT_CONTEXT.md) records academic and repository context.
- [`docs/DATA_CARD.md`](docs/DATA_CARD.md) documents dataset assumptions and local data handling.
- [`docs/MODEL_CARD.md`](docs/MODEL_CARD.md) summarizes intended use, limitations, and evaluation.
- [`docs/MLOPS.md`](docs/MLOPS.md) describes reproducibility, CI, artifacts, and experiment governance.
- [`docs/EXPERIMENTS.md`](docs/EXPERIMENTS.md) maps the original notebook into reviewable sections.
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) explains the package and folder structure.

## License

No open-source license has been declared yet. Until a license is added by the repository owner, all rights are reserved by the project author.
