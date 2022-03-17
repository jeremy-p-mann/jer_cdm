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
def result(weight):
    runner = CliRunner()
    result = runner.invoke(app, [weight])
    return result


def test_app_exit_code(result):
    assert result.exit_code == 0


def test_app_weight(weight, result):
    assert weight in result.stdout


def test_app_time(time, result):
    assert time in result.stdout
