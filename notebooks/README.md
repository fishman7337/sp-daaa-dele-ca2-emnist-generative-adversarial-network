# Notebooks

The original coursework notebook is preserved here:

```text
notebooks/DELE_CA2_A (8).ipynb
```

Generated source-only splits live in `notebooks/parts/`. They are created from the original notebook to make review and navigation easier.

Regenerate them with:

```bash
python scripts/split_notebook.py --source "notebooks/DELE_CA2_A (8).ipynb" --output notebooks/parts
```

Verify without writing files:

```bash
python scripts/split_notebook.py --source "notebooks/DELE_CA2_A (8).ipynb" --output notebooks/parts --check
```
