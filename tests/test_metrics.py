import numpy as np
import pytest

from emnist_gan.metrics import assess_mode_collapse, estimate_kid_from_features, polynomial_kernel


def test_polynomial_kernel_shape():
    x = np.ones((3, 4))
    y = np.ones((2, 4))

    kernel = polynomial_kernel(x, y)

    assert kernel.shape == (3, 2)


def test_kid_is_symmetric_for_swapped_feature_sets():
    real = np.array([[0.0, 1.0], [1.0, 0.0], [0.5, 0.5]])
    fake = np.array([[0.25, 0.75], [0.75, 0.25], [0.2, 0.8]])

    forward = estimate_kid_from_features(real, fake)
    backward = estimate_kid_from_features(fake, real)

    assert forward == pytest.approx(backward)
    assert np.isfinite(forward)


def test_assess_mode_collapse_flags_repeated_images():
    images = np.zeros((10, 2, 2, 1))

    assert assess_mode_collapse(images) == "High"
