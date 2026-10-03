import typer

from .calculator import calculate
from .converter import convert
from .errors import CalculatorError


app = typer.Typer()


@app.command()
def calc(exp: str):
    try:
        result = calculate(exp)
        typer.echo(result)
    except CalculatorError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2)


@app.command("convert")
def convert_val(
    val: str,
    unit: str = typer.Option(..., "--from"),
    to_unit: str = typer.Option(..., "--to"),
):
    try:
        result = convert(val, unit, to_unit)
        typer.echo(result)
    except CalculatorError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2)


if __name__ == "__main__":
    app()


