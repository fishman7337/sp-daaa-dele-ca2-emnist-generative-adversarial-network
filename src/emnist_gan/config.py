"""Configuration objects for repeatable EMNIST generative modeling runs."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from emnist_gan.constants import EMNIST_SELECTED_LABELS


def _env_path(name: str, default: str | Path) -> Path:
    return Path(os.getenv(name, str(default))).expanduser()


@dataclass(frozen=True)
class DatasetConfig:
    """Dataset assumptions shared by preprocessing and model-building code."""

    image_height: int = 28
    image_width: int = 28
    image_channels: int = 1
    selected_labels: tuple[int, ...] = EMNIST_SELECTED_LABELS
    source_pixel_min: float = 0.0
    source_pixel_max: float = 255.0
    target_pixel_min: float = -1.0
    target_pixel_max: float = 1.0

    @property
    def image_shape(self) -> tuple[int, int, int]:
        """Return the configured image dimensions in channels-last order."""
        return (self.image_height, self.image_width, self.image_channels)

    @property
    def num_classes(self) -> int:
        """Return the number of selected EMNIST label classes."""
        return len(self.selected_labels)


@dataclass(frozen=True)
class ModelConfig:
    """Default neural-network dimensions used by the extracted utilities."""

    latent_dim: int = 100
    dense_units: int = 256
    image_shape: tuple[int, int, int] = (28, 28, 1)
    num_classes: int = 16


@dataclass(frozen=True)
class TrainingConfig:
    """Safe defaults for local experiments and smoke tests."""

    batch_size: int = 32
    epochs: int = 100
    seed: int = 42
    learning_rate: float = 0.0002
    beta_1: float = 0.5


@dataclass(frozen=True)
class ProjectPaths:
    """Resolved project paths, optionally sourced from environment variables."""

    root: Path
    raw_data: Path
    interim_data: Path
    processed_data: Path
    artifact_dir: Path
    model_dir: Path
    log_dir: Path
    report_dir: Path

    @classmethod
    def from_env(cls) -> ProjectPaths:
        """Resolve project paths from environment variables and defaults.

        Returns:
            Absolute paths rooted at ``PROJECT_ROOT`` or the current directory.
        """
        root = _env_path("PROJECT_ROOT", ".").resolve()
        return cls(
            root=root,
            raw_data=(root / _env_path("DATA_RAW_DIR", "data/raw")).resolve(),
            interim_data=(root / _env_path("DATA_INTERIM_DIR", "data/interim")).resolve(),
            processed_data=(root / _env_path("DATA_PROCESSED_DIR", "data/processed")).resolve(),
            artifact_dir=(root / _env_path("ARTIFACT_DIR", "artifacts")).resolve(),
            model_dir=(root / _env_path("MODEL_DIR", "artifacts/models")).resolve(),
            log_dir=(root / _env_path("LOG_DIR", "artifacts/logs")).resolve(),
            report_dir=(root / _env_path("REPORT_DIR", "reports")).resolve(),
        )

    def as_dict(self) -> dict[str, Path]:
        """Return the resolved paths keyed by their configuration names."""
        return {
            "root": self.root,
            "raw_data": self.raw_data,
            "interim_data": self.interim_data,
            "processed_data": self.processed_data,
            "artifact_dir": self.artifact_dir,
            "model_dir": self.model_dir,
            "log_dir": self.log_dir,
            "report_dir": self.report_dir,
        }
