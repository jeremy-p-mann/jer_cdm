from datetime import datetime

import pytest

from jer_cdm.measurement import (MeasurementSchema, OMOPMeasurementSchema,
                                 add_measurement_row, get_measurement_data,
                                 get_measurement_row,
                                 get_mock_omop_measurement_row)
from jer_cdm.time import get_current_time


@ pytest.fixture
def measurement_df():
    return get_measurement_data()


@ pytest.fixture
def mock_measurement_df():
    return get_mock_omop_measurement_row()


@ pytest.fixture
def measurement_row(measurement_concept, ontology):
    measurement_row = get_measurement_row(
        measurement_concept,
        get_current_time(),
        115.0,
        ontology.get_unit(measurement_concept),
    )
    return measurement_row


def test_personal_data_fits_schema(measurement_df):
    MeasurementSchema.validate(measurement_df)


def test_mock_fits_schema(mock_measurement_df):
    OMOPMeasurementSchema.validate(get_mock_omop_measurement_row())


def test_make_measurement_row(measurement_row):
    MeasurementSchema.validate(measurement_row)


def test_add_measurement_row(measurement_row, measurement_df):
    new_measurement_df = add_measurement_row(
        measurement_row, measurement_df
    )
    MeasurementSchema.validate(new_measurement_df)
    assert (new_measurement_df.iloc[-1, :] == measurement_row.iloc[0, :]).all()
