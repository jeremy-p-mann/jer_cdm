import typer

from jer_cdm.time import get_current_time_str

app = typer.Typer()


# TODO: Do this as a for loop?
@app.command()
def weight(weight_in_lbs: float):
    time = get_current_time_str()
    typer.echo(f"Log weight {weight_in_lbs} at {time}")


@app.command('sud')
def sud(
    sud_level: int = typer.Argument(..., min=0, max=10),
):
    time = get_current_time_str()
    typer.echo(f"Log Subjective Units of Distress (SUD) {sud_level} at {time}")


if __name__ == "__main__":
    app()
