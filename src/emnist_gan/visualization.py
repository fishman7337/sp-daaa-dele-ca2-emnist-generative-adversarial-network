"""Plotting helpers for generated EMNIST samples."""

from __future__ import annotations

from pathlib import Path

import numpy as np
from numpy.typing import ArrayLike, NDArray


def make_image_grid(images: ArrayLike, rows: int, cols: int) -> NDArray[np.float32]:
    """Arrange grayscale images into a single image grid array."""
    if rows <= 0 or cols <= 0:
        raise ValueError("rows and cols must be positive")
    array = np.asarray(images, dtype=np.float32)
    if array.ndim == 4 and array.shape[-1] == 1:
        array = array[..., 0]
    if array.ndim != 3:
        raise ValueError("images must have shape (N, H, W) or (N, H, W, 1)")
    if array.shape[0] < rows * cols:
        raise ValueError("not enough images to fill the requested grid")

    selected = array[: rows * cols]
    grid_rows = [
        np.concatenate(selected[row * cols : (row + 1) * cols], axis=1) for row in range(rows)
    ]
    return np.concatenate(grid_rows, axis=0)


def save_image_grid(images: ArrayLike, output_path: str | Path, rows: int, cols: int) -> Path:
    """Save a generated sample grid using matplotlib when available."""
    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise ImportError("matplotlib is required to save image grids") from exc

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    grid = make_image_grid(images, rows=rows, cols=cols)
    plt.imsave(path, grid, cmap="gray")
    return path
