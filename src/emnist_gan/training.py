"""Training helpers that keep experiments reproducible and easy to smoke test."""

from __future__ import annotations

import random
from typing import Literal

import numpy as np
from numpy.typing import NDArray


def set_random_seed(seed: int = 42) -> None:
    """Seed Python, NumPy, and TensorFlow when TensorFlow is installed."""

    random.seed(seed)
    np.random.seed(seed)
    try:
        import tensorflow as tf
    except ImportError:
        return
    tf.random.set_seed(seed)


def make_latent_vectors(
    num_samples: int,
    latent_dim: int,
    seed: int | None = None,
    distribution: Literal["normal", "uniform"] = "normal",
) -> NDArray[np.float32]:
    """Create deterministic latent vectors for generator smoke tests and sampling."""

    if num_samples <= 0:
        raise ValueError("num_samples must be positive")
    if latent_dim <= 0:
        raise ValueError("latent_dim must be positive")

    rng = np.random.default_rng(seed)
    if distribution == "normal":
        values = rng.normal(size=(num_samples, latent_dim))
    elif distribution == "uniform":
        values = rng.uniform(-1.0, 1.0, size=(num_samples, latent_dim))
    else:
        raise ValueError("distribution must be either 'normal' or 'uniform'")
    return values.astype(np.float32)
