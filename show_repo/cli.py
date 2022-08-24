import pathlib
import click
from show_repo.show_repo import get_dir_items, get_output


@click.command()
@click.argument("dir", default=".", type=click.Path(exists=True))
def cli(dir: click.Path) -> None:
    dir_items = get_dir_items(pathlib.Path(dir))
    print(get_output(dir_items))
