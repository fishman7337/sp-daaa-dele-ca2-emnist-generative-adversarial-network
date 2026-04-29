import numpy as np
import pytest

from emnist_gan.training import make_latent_vectors


def test_make_latent_vectors_is_deterministic():
    first = make_latent_vectors(4, 3, seed=42)
    second = make_latent_vectors(4, 3, seed=42)

    np.testing.assert_array_equal(first, second)


def test_make_latent_vectors_rejects_unknown_distribution():
    with pytest.raises(ValueError, match="distribution"):
        make_latent_vectors(4, 3, distribution="triangle")
