# Architecture

## Package

`src/emnist_gan` contains lightweight utilities extracted from the original notebook:

- `config.py`: dataclass-based configuration for dataset, model, training, and project paths.
- `constants.py`: selected EMNIST labels and class mappings.
- `data.py`: preprocessing, orientation correction, relabeling, one-hot encoding, and class counts.
- `metrics.py`: lightweight KID kernel and mode-collapse helpers.
- `training.py`: seed control and latent vector generation.
- `visualization.py`: image-grid utilities.
- `models/gan.py`: optional TensorFlow/Keras dense GAN builders.

TensorFlow is optional so tests and CI can run quickly. Model builders raise a clear error if TensorFlow is not installed.

## Folders

- `data/`: local dataset staging only.
- `artifacts/`: local checkpoints and logs only.
- `reports/figures/`: local generated visualizations.
- `notebooks/parts/`: generated source-only notebooks.
- `docs/`: project documentation.
- `tests/`: fast unit tests for reusable code.

## Design Choices

- Keep the original notebook intact for coursework traceability.
- Extract only stable, reusable logic into Python modules.
- Avoid putting large datasets or checkpoints into git.
- Keep CI focused on reviewable code, documentation integrity, and security checks.
