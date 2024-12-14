"""Console script for rephrasinator."""

import typer
from rich.console import Console

import rephrasinator

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for rephrasinator."""
    console.print(
        "Replace this message by putting your code into " "rephrasinator.cli.main",
    )
    console.print("See Typer documentation at https://typer.tiangolo.com/")


if __name__ == "__main__":
    app()
