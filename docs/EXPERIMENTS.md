# Experiments

The original notebook is large, so `scripts/split_notebook.py` breaks it into source-only sections for easier review.

## Notebook Sections

| Section | Description |
| --- | --- |
| 00 | Project overview and background research |
| 01 | Library imports |
| 02 | Dataset loading, preprocessing, and augmentation |
| 03 | Exploratory data analysis and visualization |
| 04 | GAN training for non-augmented EMNIST data |
| 05 | GAN training for augmented EMNIST data |
| 06 | Model evaluation, cDRAGAN, and VAE comparison |
| 07 | Best model architecture visualization and complexity |
| 08 | Bibliography |

## Regenerating Notebook Parts

```bash
python scripts/split_notebook.py --source "notebooks/DELE_CA2_A (8).ipynb" --output notebooks/parts
```

To verify committed split notebooks match the original notebook source:

```bash
python scripts/split_notebook.py --source "notebooks/DELE_CA2_A (8).ipynb" --output notebooks/parts --check
```

## Review Policy

- Review notebook source and markdown rather than large output diffs.
- Keep expensive full training outside CI.
- Promote stable, reusable notebook functions into `src/emnist_gan` with tests.
