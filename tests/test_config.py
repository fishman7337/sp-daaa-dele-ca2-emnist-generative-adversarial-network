from pathlib import Path

from emnist_gan.config import DatasetConfig, ProjectPaths


def test_dataset_config_matches_coursework_selected_classes():
    config = DatasetConfig()

    assert config.image_shape == (28, 28, 1)
    assert config.num_classes == 16
    assert config.selected_labels == (1, 2, 4, 5, 6, 7, 9, 10, 12, 14, 15, 16, 17, 20, 24, 26)


def test_project_paths_resolve_from_environment(monkeypatch, tmp_path):
    monkeypatch.setenv("PROJECT_ROOT", str(tmp_path))
    monkeypatch.setenv("DATA_RAW_DIR", "raw")

    paths = ProjectPaths.from_env()

    assert paths.root == tmp_path.resolve()
    assert paths.raw_data == (tmp_path / "raw").resolve()
    assert isinstance(paths.as_dict()["model_dir"], Path)
