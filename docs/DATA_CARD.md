# Data Card

## Dataset

The project works with selected EMNIST letter classes. The original notebook filters and relabels the following original EMNIST labels:

```text
1, 2, 4, 5, 6, 7, 9, 10, 12, 14, 15, 16, 17, 20, 24, 26
```

These are mapped to contiguous class indices for:

```text
A, B, D, E, F, G, I, J, L, N, O, P, Q, T, X, Z
```

## Preprocessing

The reusable package includes helpers for:

- Adding a channel axis to grayscale images.
- Scaling pixels from `[0, 255]` to `[-1, 1]`.
- Correcting EMNIST orientation by rotating 90 degrees clockwise and mirroring left-to-right.
- Relabeling selected EMNIST classes to zero-based indices.
- One-hot encoding labels without requiring TensorFlow.

## Local Data Policy

Dataset files should be stored locally under `data/raw/` and should not be committed. Intermediate and processed files belong under `data/interim/` and `data/processed/`.

The repository tracks only `.gitkeep` placeholders for these folders.

## Known Limitations

- The original notebook is coursework research code and may contain Colab-specific paths or cells.
- Full training requires substantial compute and is intentionally not part of the default CI workflow.
- Generated data quality should be assessed with both quantitative metrics and visual review.
