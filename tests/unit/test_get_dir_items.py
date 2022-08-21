from git_list import git_list
from pathlib import Path


def test_dir_items():
    """Check if function returns list of git_list.DirItem"""
    assert set(
        [
            isinstance(item, git_list.DirItem)
            for item in git_list.get_dir_items(Path("."))
        ]
    ) == {True}
