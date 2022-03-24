import typer
import pandas as pd

from jer_cdm.concepts import MeasurementConcept, Ontology
from jer_cdm.measurement import (add_measurement_row, get_measurement_data,
                                 get_measurement_row, write_measurement_df)
from jer_cdm.time import get_current_time, get_current_time_str

app = typer.Typer()
ONTOLOGY = Ontology()


# TODO: Do this as a for loop?
@app.command()
def weight(weight_in_lbs: float):
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


@app.command('sud')
def sud(
    sud_level: int = typer.Argument(..., min=0, max=10),
):
    time = get_current_time_str()
    typer.echo(f"Log Subjective Units of Distress (SUD) {sud_level} at {time}")


if __name__ == "__main__":
    app()
