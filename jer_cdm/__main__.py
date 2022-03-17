import typer

app = typer.Typer()


@app.command()
def weight(weight: float):
    typer.echo(f"Logging Weight {weight}")


if __name__ == "__main__":
    app()
