"""Command-line entrypoint for project health checks."""

from __future__ import annotations

import argparse

from emnist_gan import __version__
from emnist_gan.config import DatasetConfig, ProjectPaths


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="EMNIST generative modeling project utilities")
    parser.add_argument("--version", action="store_true", help="print the package version")
    parser.add_argument("--show-paths", action="store_true", help="print resolved project paths")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.version:
        print(__version__)
        return 0

    dataset = DatasetConfig()
    print(
        "EMNIST Generative Modeling "
        f"({dataset.num_classes} selected classes, image shape {dataset.image_shape})"
    )

    if args.show_paths:
        for name, path in ProjectPaths.from_env().as_dict().items():
            print(f"{name}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
