import pytest

from jer_cdm.measurement import MeasurementSchema, get_mock_measurement_row


@pytest.fixture
def measurement_df():
    return get_mock_measurement_row()


def test_mock_fits_schema(measurement_df):
    MeasurementSchema.validate(get_mock_measurement_row())
