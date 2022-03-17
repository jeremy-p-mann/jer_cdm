from jer_cdm.time import get_current_time_str
from datetime import datetime


def test_current_time():
    actual_time = datetime.now().strftime('%Y-%m-%dT%H:%M%Z')
    assert get_current_time_str() == actual_time
