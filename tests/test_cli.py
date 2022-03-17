import pytest
from typer.testing import CliRunner

from jer_cdm.__main__ import app
from jer_cdm.time import get_current_time_str


@pytest.fixture(scope='session')
def weight():
    weight = str(180.0)
    return weight


@pytest.fixture(scope='session')
def time():
    return get_current_time_str()


@pytest.fixture(scope='session')
def log_weight_result(weight):
    runner = CliRunner()
    return runner.invoke(app, [weight])


def test_app_exit_code(log_weight_result):
    assert log_weight_result.exit_code == 0


def test_app_weight(weight, log_weight_result):
    assert weight in log_weight_result.stdout


def test_app_time(time, log_weight_result):
    assert time in log_weight_result.stdout
