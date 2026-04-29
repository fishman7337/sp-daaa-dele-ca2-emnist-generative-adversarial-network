"""Data preparation utilities extracted from the original notebook."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

import numpy as np
from numpy.typing import ArrayLike, NDArray

from emnist_gan.constants import EMNIST_SELECTED_LABELS


def ensure_channel_axis(images: ArrayLike) -> NDArray[np.float32]:
    """Return images as a four-dimensional array: batch, height, width, channel."""

    array = np.asarray(images)
    if array.ndim == 2:
        array = array[np.newaxis, :, :, np.newaxis]
    elif array.ndim == 3:
        array = array[:, :, :, np.newaxis]
    elif array.ndim != 4:
        raise ValueError("images must have shape (H, W), (N, H, W), or (N, H, W, C)")
    return array.astype(np.float32, copy=False)


def normalise_images(
    images: ArrayLike,
    source_range: tuple[float, float] = (0.0, 255.0),
    target_range: tuple[float, float] = (-1.0, 1.0),
) -> NDArray[np.float32]:
    """Scale image pixels from a source range to the target range used by tanh GANs."""

    source_min, source_max = source_range
    target_min, target_max = target_range
    if source_max <= source_min:
        raise ValueError("source_range maximum must be greater than minimum")
    if target_max <= target_min:
        raise ValueError("target_range maximum must be greater than minimum")

    array = ensure_channel_axis(images)
    array = (array - source_min) / (source_max - source_min)
    array = np.clip(array, 0.0, 1.0)
    return (array * (target_max - target_min) + target_min).astype(np.float32)


def fix_image_orientation(images: ArrayLike) -> NDArray[np.float32]:
    """Rotate EMNIST images 90 degrees clockwise and mirror them left-to-right."""

    array = np.asarray(images)
    if array.ndim == 2:
        fixed = np.fliplr(np.rot90(array, k=-1))
    elif array.ndim in {3, 4}:
        fixed = np.flip(np.rot90(array, k=-1, axes=(1, 2)), axis=2)
    else:
        raise ValueError("images must have shape (H, W), (N, H, W), or (N, H, W, C)")
    return fixed.astype(np.float32, copy=False)


def relabel_selected_letters(
    labels: ArrayLike,
    selected_labels: Iterable[int] = EMNIST_SELECTED_LABELS,
) -> NDArray[np.int64]:
    """Map original EMNIST letter labels to contiguous zero-based class indices."""

    mapping = {original_label: index for index, original_label in enumerate(selected_labels)}
    labels_array = np.asarray(labels).astype(int, copy=False)
    unknown_labels = sorted(set(labels_array.tolist()) - set(mapping))
    if unknown_labels:
        raise ValueError(
            f"labels contain values outside the selected EMNIST classes: {unknown_labels}"
        )
    return np.vectorize(mapping.__getitem__)(labels_array).astype(np.int64)


def one_hot(labels: ArrayLike, num_classes: int | None = None) -> NDArray[np.float32]:
    """One-hot encode integer labels without requiring TensorFlow/Keras."""

    labels_array = np.asarray(labels).astype(int, copy=False)
    if labels_array.ndim != 1:
        raise ValueError("labels must be a one-dimensional array")
    if labels_array.size == 0:
        raise ValueError("labels cannot be empty")

    inferred_classes = int(labels_array.max()) + 1
    class_count = num_classes or inferred_classes
    if class_count < inferred_classes:
        raise ValueError("num_classes is smaller than the largest label index")

    encoded = np.zeros((labels_array.size, class_count), dtype=np.float32)
    encoded[np.arange(labels_array.size), labels_array] = 1.0
    return encoded


def class_counts(labels: ArrayLike, class_names: dict[int, str] | None = None) -> dict[Any, int]:
    """Return class counts using optional human-readable class names."""

    labels_array = np.asarray(labels).astype(int, copy=False)
    counts = np.bincount(labels_array)
    if class_names is None:
        return {index: int(count) for index, count in enumerate(counts) if count > 0}
    return {
        class_names.get(index, index): int(count) for index, count in enumerate(counts) if count > 0
    }
