from git_list import git_list


def test_valid_repo_is_valid():
    """Check if current working directory is repo"""
    assert git_list.valid_repo(".")


def test_valid_repo_not_valid():
    """Ensure tests directory is not valid repo"""
    assert not git_list.valid_repo("tests")
