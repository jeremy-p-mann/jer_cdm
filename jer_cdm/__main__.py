import typer

from jer_cdm.time import get_current_time_str

app = typer.Typer()


@app.command()
def weight(weight_in_lbs: float):
    time = get_current_time_str()
    typer.echo(f"Log Weight {weight} at {time}")


@app.command('thc')
def thc(thc_in_mg: float):
    time = get_current_time_str()
    typer.echo(f"Log Weight {weight} at {time}")


if __name__ == "__main__":
    app()
