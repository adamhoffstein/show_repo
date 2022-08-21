from show_repo import show_repo
from pathlib import Path


def test_dir_items():
    """Check if function returns list of git_list.DirItem"""
    assert set(
        [
            isinstance(item, show_repo.DirItem)
            for item in show_repo.get_dir_items(Path("."))
        ]
    ) == {True}
