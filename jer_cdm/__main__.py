import typer

from jer_cdm.time import get_current_time_str

app = typer.Typer()


# TODO: Do this as a for loop?
@app.command()
def weight(weight_in_lbs: float):
    time = get_current_time_str()
    typer.echo(f"Log weight {weight_in_lbs} at {time}")


@app.command('thc')
def thc(thc_in_mg: float):
    time = get_current_time_str()
    typer.echo(f"Log THC {thc_in_mg} at {time}")


@app.command('cbd')
def cbd(cbd_in_mg: float):
    time = get_current_time_str()
    typer.echo(f"Log CBD {cbd_in_mg} at {time}")


if __name__ == "__main__":
    app()
