"""Reusable utilities for the EMNIST generative modeling coursework project."""

from emnist_gan.config import DatasetConfig, ModelConfig, ProjectPaths, TrainingConfig
from emnist_gan.constants import EMNIST_SELECTED_LABELS, INDEX_TO_LETTER, LABEL_TO_INDEX
from emnist_gan.data import (
    class_counts,
    ensure_channel_axis,
    fix_image_orientation,
    normalise_images,
    one_hot,
    relabel_selected_letters,
)

__all__ = [
    "DatasetConfig",
    "EMNIST_SELECTED_LABELS",
    "INDEX_TO_LETTER",
    "LABEL_TO_INDEX",
    "ModelConfig",
    "ProjectPaths",
    "TrainingConfig",
    "class_counts",
    "ensure_channel_axis",
    "fix_image_orientation",
    "normalise_images",
    "one_hot",
    "relabel_selected_letters",
]

__version__ = "0.1.0"
