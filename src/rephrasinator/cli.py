import typer
from rich.console import Console

from rephrasinator import rephrasinator

app = typer.Typer()
console = Console()


@app.command()
def list_models():
    console.print("Available models:")
    for model in rephrasinator.LLMModel:
        console.print(f"- {model.name}")


@app.command()
def text(
    text: str = typer.Argument(..., help="Text to rephrase"),
    model: str = typer.Option(..., "--model", "-m", help="Model to use for rephrasing"),
    style: str = typer.Option(..., "--style", "-s", help="Style of rephrasing"),
):
    console.print(f"Rephrasing: {text}, with model: {model}, in style: {style}")
    rephrased_text = rephrasinator.get_rephrased_sentence(text, style)
    console.print(rephrased_text)


if __name__ == "__main__":
    app()
