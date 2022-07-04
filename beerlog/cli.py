import typer
from beerlog.core import add_beer_to_db, get_beer_from_db
from typing import Optional
from rich.table import Table
from rich.console import Console


main = typer.Typer(help="Beer Management Application")

console = Console()


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a news beer to database."""
    if add_beer_to_db(name, style, flavor, image, cost):
        print("\N{beer mug} beer added to database.")
    else:
        print("\N{no entry} something went wrong.")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """Lists beers from a new style."""
    beers = get_beer_from_db()
    table = Table(title="BeerLog \N{beer mug}")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header, style="blue")

    for beer in beers:
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
