import pandas as pd
import typer

from jer_cdm.concepts import MeasurementConcept, Ontology, PhysicalConcept
from jer_cdm.measurement import (add_measurement_row, get_measurement_data,
                                 get_measurement_row, write_measurement_df)
from jer_cdm.time import get_current_time, get_current_time_str

app = typer.Typer()
ONTOLOGY = Ontology()

# TODO: Do this as a for loop?


@app.command('log_weight')
def log_weight(
    weight_in_lbs: float,
    confirm: bool = typer.Option(True)
):
    if confirm:
        delete = typer.confirm(
            f"Confirm logging body weight {weight_in_lbs} lbs",
            default=True
        )
        if not delete:
            typer.echo("Aborting log")
            raise typer.Abort()
    time_str = get_current_time_str()
    measurement_df = get_measurement_data()
    weight_concept = ONTOLOGY.get_concept_from_id(
        MeasurementConcept.BODY_WEIGHT)
    new_row = get_measurement_row(
        weight_concept,
        pd.Timestamp(time_str),
        weight_in_lbs,
        ONTOLOGY.get_unit(weight_concept),
    )
    new_measurement_df = add_measurement_row(
        new_row, measurement_df
    )
    write_measurement_df(new_measurement_df)
    typer.echo(f"Log weight {weight_in_lbs} at {time_str}")


@app.command('show_weight')
def show_weight(
    n_measurents: int = typer.Argument(..., min=0, ),
):
    time = get_current_time_str()
    measurement_df = get_measurement_data()
    weight_df = measurement_df[
        measurement_df.measurement_concept_id == MeasurementConcept.BODY_WEIGHT
    ][['datetime', 'value']]
    n = min(len(weight_df), n_measurents)
    typer.echo(f"Show last {n_measurents} weight measurements before {time} ")
    typer.echo(weight_df.tail(n))


if __name__ == "__main__":
    app()
