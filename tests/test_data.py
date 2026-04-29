import numpy as np
import pytest

from emnist_gan.constants import INDEX_TO_LETTER
from emnist_gan.data import (
    class_counts,
    ensure_channel_axis,
    fix_image_orientation,
    normalise_images,
    one_hot,
    relabel_selected_letters,
)


def test_ensure_channel_axis_accepts_single_image():
    image = np.zeros((28, 28))

    result = ensure_channel_axis(image)

    assert result.shape == (1, 28, 28, 1)
    assert result.dtype == np.float32


def test_normalise_images_scales_to_tanh_range():
    images = np.array([[[0.0, 127.5, 255.0]]])

    result = normalise_images(images)

    assert result.shape == (1, 1, 3, 1)
    np.testing.assert_allclose(result[0, 0, :, 0], [-1.0, 0.0, 1.0])


def test_fix_image_orientation_matches_notebook_rotate_and_mirror():
    images = np.array([[[[1], [2]], [[3], [4]]]], dtype=np.float32)

    result = fix_image_orientation(images)

    expected = np.array([[[[1], [3]], [[2], [4]]]], dtype=np.float32)
    np.testing.assert_array_equal(result, expected)


def test_relabel_selected_letters_uses_zero_based_indices():
    labels = np.array([1, 2, 4, 26])

    result = relabel_selected_letters(labels)

    np.testing.assert_array_equal(result, [0, 1, 2, 15])


def test_relabel_selected_letters_rejects_unselected_labels():
    with pytest.raises(ValueError, match="outside the selected"):
        relabel_selected_letters([1, 3])


def test_one_hot_and_class_counts():
    labels = np.array([0, 1, 1, 15])

    encoded = one_hot(labels, num_classes=16)
    counts = class_counts(labels, INDEX_TO_LETTER)

    assert encoded.shape == (4, 16)
    assert encoded[0, 0] == 1.0
    assert counts == {"A": 1, "B": 2, "Z": 1}
