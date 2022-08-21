from show_repo import show_repo


def test_valid_repo_is_valid():
    """Check if current working directory is repo"""
    assert show_repo.valid_repo(".")


def test_valid_repo_not_valid():
    """Ensure tests directory is not valid repo"""
    assert not show_repo.valid_repo("tests")
