.PHONY: install install-dev test lint format security split-notebooks

install:
	python -m pip install --upgrade pip
	python -m pip install -e .

install-dev:
	python -m pip install --upgrade pip
	python -m pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

format:
	ruff format .

security:
	bandit -q -r src scripts
	pip-audit -r requirements.txt -r requirements-dev.txt

split-notebooks:
	python scripts/split_notebook.py --source "notebooks/DELE_CA2_A (8).ipynb" --output notebooks/parts
