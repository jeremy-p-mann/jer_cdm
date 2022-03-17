import pytest
from typer.testing import CliRunner

from jer_cdm.__main__ import app
from jer_cdm.time import get_current_time_str

# TODO REFACTOR TO ENUM
LOG_PAIRS = {
    'weight': 149.0,
    'thc': 2.5,
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
    return runner.invoke(app, cmd)


def test_app_exit_code(log_result):
    assert log_result.exit_code == 0, \
        f'log_result.{log_result.stdout}'


def test_app_echos_name(name, log_result):
    assert name in log_result.stdout.lower(), \
        f'log_result.{log_result.stdout}'


def test_app_echos_value(value, log_result):
    assert value in log_result.stdout.lower(), \
        f'log_result.{log_result.stdout}'


def test_app_echos_time(time, log_result):
    assert time in log_result.stdout, \
        f'log_result.{log_result.stdout}'
