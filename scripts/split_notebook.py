"""Split the preserved coursework notebook into reviewable source-only notebooks."""

from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path
from typing import Any

TOP_LEVEL_SECTION = re.compile(r"^#\s+(.+?)\s*$")
NUMBERED_SECTION = re.compile(r"^\d+\.\s+")


def parse_args() -> argparse.Namespace:
    """Parse source, output, and verification options."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True, help="path to the source .ipynb file")
    parser.add_argument("--output", type=Path, required=True, help="directory for split notebooks")
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify existing split notebooks instead of writing them",
    )
    return parser.parse_args()


def read_notebook(path: Path) -> dict[str, Any]:
    """Load a notebook JSON document.

    Args:
        path: Notebook path.

    Returns:
        Parsed notebook mapping.
    """
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def serialise_notebook(notebook: dict[str, Any]) -> str:
    """Serialize a notebook deterministically with a trailing newline."""
    return json.dumps(notebook, ensure_ascii=False, indent=2) + "\n"


def extract_section_title(cell: dict[str, Any]) -> str | None:
    """Extract a recognized top-level section title from a markdown cell.

    Args:
        cell: Notebook cell to inspect.

    Returns:
        A recognized section title, or ``None`` for non-section cells.
    """
    if cell.get("cell_type") != "markdown":
        return None
    source = "".join(cell.get("source", []))
    for line in source.splitlines():
        match = TOP_LEVEL_SECTION.match(line.strip())
        if not match:
            continue
        title = match.group(1).strip()
        if title.startswith("ST1504") or NUMBERED_SECTION.match(title):
            return title
    return None


def slugify(title: str, section_index: int) -> str:
    """Build a stable, ordered filename stem for a notebook section.

    Args:
        title: Human-readable section title.
        section_index: Zero-based section order.

    Returns:
        A filesystem-safe stem prefixed with the section order.
    """
    if title.startswith("ST1504"):
        clean_title = "project overview"
    else:
        clean_title = NUMBERED_SECTION.sub("", title)
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", clean_title.lower()).strip("_")
    return f"{section_index:02d}_{slug or 'section'}"


def clean_cell(cell: dict[str, Any]) -> dict[str, Any]:
    """Copy a cell while removing execution state from code cells.

    Args:
        cell: Source notebook cell.

    Returns:
        A deep-copied, source-only cell.
    """
    cleaned = copy.deepcopy(cell)
    if cleaned.get("cell_type") == "code":
        cleaned["execution_count"] = None
        cleaned["outputs"] = []
    return cleaned


def split_notebook(source: Path) -> dict[str, dict[str, Any]]:
    """Split a source notebook at recognized top-level headings.

    Args:
        source: Preserved coursework notebook path.

    Returns:
        Generated filenames mapped to source-only notebook documents.
    """
    notebook = read_notebook(source)
    base_metadata = copy.deepcopy(notebook.get("metadata", {}))
    sections: list[tuple[str, list[dict[str, Any]]]] = []

    for cell in notebook.get("cells", []):
        title = extract_section_title(cell)
        if title is not None or not sections:
            section_title = title or "Project Overview"
            sections.append((section_title, []))
        sections[-1][1].append(clean_cell(cell))

    split: dict[str, dict[str, Any]] = {}
    for section_index, (title, cells) in enumerate(sections):
        metadata = copy.deepcopy(base_metadata)
        metadata["split_from"] = source.as_posix()
        metadata["split_section"] = title
        split[f"{slugify(title, section_index)}.ipynb"] = {
            "cells": cells,
            "metadata": metadata,
            "nbformat": notebook.get("nbformat", 4),
            "nbformat_minor": notebook.get("nbformat_minor", 5),
        }
    return split


def write_split_notebooks(split: dict[str, dict[str, Any]], output_dir: Path) -> None:
    """Write current section notebooks and remove obsolete generated sections.

    Args:
        split: Generated filenames mapped to notebook documents.
        output_dir: Destination directory for generated notebooks.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    expected_names = set(split)

    for file_name, notebook in split.items():
        (output_dir / file_name).write_text(serialise_notebook(notebook), encoding="utf-8")

    for existing in output_dir.glob("*.ipynb"):
        if existing.name not in expected_names:
            existing.unlink()


def check_split_notebooks(split: dict[str, dict[str, Any]], output_dir: Path) -> int:
    """Check committed section notebooks against freshly generated content.

    Args:
        split: Expected filenames mapped to notebook documents.
        output_dir: Directory containing committed section notebooks.

    Returns:
        ``0`` when every generated file matches, otherwise ``1``.
    """
    missing_or_changed: list[str] = []
    for file_name, notebook in split.items():
        path = output_dir / file_name
        expected = serialise_notebook(notebook)
        if not path.exists() or path.read_text(encoding="utf-8") != expected:
            missing_or_changed.append(file_name)

    stale = sorted(path.name for path in output_dir.glob("*.ipynb") if path.name not in split)
    if missing_or_changed or stale:
        print("Split notebooks are out of date.")
        if missing_or_changed:
            print("Missing or changed:")
            for file_name in missing_or_changed:
                print(f"  - {file_name}")
        if stale:
            print("Stale:")
            for file_name in stale:
                print(f"  - {file_name}")
        return 1

    print(f"Split notebooks are up to date ({len(split)} files).")
    return 0


def main() -> int:
    """Generate section notebooks or verify their committed state."""
    args = parse_args()
    split = split_notebook(args.source)
    if args.check:
        return check_split_notebooks(split, args.output)
    write_split_notebooks(split, args.output)
    print(f"Wrote {len(split)} split notebooks to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
