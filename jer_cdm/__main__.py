import typer

from jer_cdm.time import get_current_time_str

app = typer.Typer()


@app.command()
def weight(weight: float):
    time = get_current_time_str()
    typer.echo(f"Log Weight {weight} at {time}")


if __name__ == "__main__":
    app()
