import typer
from rich.console import Console

from rephrasinator import rephrasinator
from rephrasinator.model import get_model_by_name

app = typer.Typer()
console = Console()


@app.command()
def list_models():
    console.print("Available models:")
    for model in rephrasinator.LLMModel:
        console.print(f"- {model.value}")


@app.command()
def text(
    text: str = typer.Argument(..., help="Text to rephrase"),
    model: str = typer.Option(..., "--model", "-m", help="Model to use for rephrasing"),
    additional_request: str = typer.Option(
        ...,
        "--additional_request",
        "-s",
        help="Additional request to rephrasing style",
    ),
):
    console.print(
        f"Rephrasing: {text}, with model: {model}, in with additional request: {additional_request}",
    )
    model = get_model_by_name(model)
    rephrased_text = rephrasinator.get_rephrased_sentence(
        text,
        additional_request,
        model,
    )
    console.print(rephrased_text)


if __name__ == "__main__":
    app()
