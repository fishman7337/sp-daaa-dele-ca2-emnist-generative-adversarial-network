"""Lightweight evaluation helpers that do not require heavyweight ML dependencies."""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray


def polynomial_kernel(features_x: ArrayLike, features_y: ArrayLike) -> NDArray[np.float64]:
    """Compute the cubic polynomial kernel used by the KID metric."""
    x = np.asarray(features_x, dtype=np.float64)
    y = np.asarray(features_y, dtype=np.float64)
    if x.ndim != 2 or y.ndim != 2:
        raise ValueError("features must be two-dimensional arrays")
    if x.shape[1] != y.shape[1]:
        raise ValueError("feature dimensions must match")
    feature_dim = x.shape[1]
    return (x @ y.T / feature_dim + 1.0) ** 3


def estimate_kid_from_features(real_features: ArrayLike, fake_features: ArrayLike) -> float:
    """Estimate unbiased KID from precomputed feature embeddings.

    The unbiased finite-sample estimate can be slightly negative for very small
    sample sizes, even when the two feature sets are identical.
    """
    real = np.asarray(real_features, dtype=np.float64)
    fake = np.asarray(fake_features, dtype=np.float64)
    if real.shape[0] < 2 or fake.shape[0] < 2:
        raise ValueError("at least two real and fake samples are required")

    real_kernel = polynomial_kernel(real, real)
    fake_kernel = polynomial_kernel(fake, fake)
    cross_kernel = polynomial_kernel(real, fake)
    np.fill_diagonal(real_kernel, 0.0)
    np.fill_diagonal(fake_kernel, 0.0)

    m = real.shape[0]
    n = fake.shape[0]
    return float(
        real_kernel.sum() / (m * (m - 1))
        + fake_kernel.sum() / (n * (n - 1))
        - 2.0 * cross_kernel.mean()
    )


def assess_mode_collapse(images: ArrayLike, threshold: float = 0.9, decimals: int = 0) -> str:
    """Flag likely mode collapse by comparing rounded unique samples to total samples."""
    if not 0.0 < threshold <= 1.0:
        raise ValueError("threshold must be in the interval (0, 1]")
    array = np.asarray(images)
    if array.ndim < 2:
        raise ValueError("images must contain at least a sample and feature dimension")
    flattened = np.round(array.reshape(array.shape[0], -1), decimals=decimals)
    unique_ratio = np.unique(flattened, axis=0).shape[0] / array.shape[0]
    return "Low" if unique_ratio >= threshold else "High"
