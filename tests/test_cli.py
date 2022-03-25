import pytest
import pandas as pd
from typer.testing import CliRunner

from jer_cdm.__main__ import app
from jer_cdm.measurement import (get_measurement_data, write_measurement_df,
                                 get_measurement_data_filepath)
from jer_cdm.time import get_current_time_str

# TODO REFACTOR TO ENUM
LOG_PAIRS = {
    'log_weight': 149.923485912,
    'show_weight': 2,
}


@pytest.fixture(scope='session', params=LOG_PAIRS.keys())
def name(request):
    return request.param


@pytest.fixture(scope='session')
def value(name):
    return LOG_PAIRS[name]


@pytest.fixture(scope='session')
def time():
    return get_current_time_str()


@pytest.fixture(scope='session')
def log_result(name, value):
    runner = CliRunner()
    cmd = [name, str(value)]
    if 'log' in name.split('_'):
        cmd += ['--no-confirm']
    original_measurement_df = get_measurement_data()
    yield runner.invoke(app, cmd)
    write_measurement_df(original_measurement_df)
    new_measurement_df = get_measurement_data()
    assert (new_measurement_df == original_measurement_df).all(axis=None)


def test_app_exit_code(log_result):
    assert log_result.exit_code == 0, \
        f'log_result.{log_result.stdout}'


def test_app_echos_name(name, log_result):
    assert set(name.split('_')).issubset(
        set(log_result.stdout.lower().split(' '))
    ), f'log_result.{log_result.stdout}'


def test_app_echos_value(value, log_result):
    assert str(value) in log_result.stdout.lower(), \
        f'log_result.{log_result.stdout}'


def test_app_echos_time(time, log_result):
    assert time in log_result.stdout, \
        f'log_result.{log_result.stdout}'


def test_measurement_logged_correctly(time, ontology, log_result, name, value):
    # concept = ontology.get_concept_from_endpoint(value)
    # unit = ontology.get_unit(concept)
    if 'log' in name.split('_'):
        measurement_df = get_measurement_data()
        assert measurement_df['datetime'].iloc[-1] == pd.Timestamp(time)
        assert measurement_df['value'].iloc[-1] == value
    # assert measurement_df['measurement_concept_id'].iloc[-1] == concept.value
    # assert measurement_df['unit_concept_id'].iloc[-1] == unit.value
    # TODO: test unit concept id
