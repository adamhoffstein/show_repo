import argparse
import pathlib
from dataclasses import dataclass
from typing import Generator, List
from git import Repo
from git.exc import InvalidGitRepositoryError
from colorama import Fore
from tabulate import tabulate


@dataclass
class DirItem:
    name: str
    repo: bool = False
    directory: bool = False
    dirty: bool = False

    @property
    def color(self) -> str:
        if self.repo and self.directory and self.dirty:
            return Fore.RED
        elif self.repo and self.directory and not self.dirty:
            return Fore.GREEN
        elif not self.repo and self.directory:
            return Fore.BLUE
        else:
            return Fore.WHITE

    @property
    def output(self) -> str:
        return self.color + self.name


def chunks(l: list, n: int) -> Generator[list, None, None]:
    for i in range(0, len(l), n):
        yield l[i : i + n]


def valid_repo(path: pathlib.Path) -> Repo:
    try:
        return Repo(path)
    except InvalidGitRepositoryError:
        pass


def get_output(items: List[DirItem]) -> str:
    dir_output = []
    cols = 6
    for item in list(chunks([d.output for d in items], cols)):
        dir_output.append(item)
    return tabulate(dir_output, headers="firstrow", tablefmt="plain")


def get_dir_items(dir: pathlib.Path) -> List[DirItem]:
    results = []
    for d in dir.iterdir():
        if d.is_dir():
            if repo := valid_repo(d):
                results.append(
                    DirItem(
                        name=d.name,
                        repo=True,
                        directory=True,
                        dirty=repo.is_dirty(untracked_files=True),
                    )
                )
            else:
                results.append(
                    DirItem(
                        name=d.name,
                        directory=True,
                    )
                )
        else:
            results.append(
                DirItem(
                    name=d.name,
                )
            )
    return results


def cli() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", nargs="?", default=".", type=pathlib.Path)
    args = parser.parse_args()
    dir_items = get_dir_items(args.dir)
    print(get_output(dir_items))
