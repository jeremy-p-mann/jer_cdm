from datetime import datetime


def get_datetime_format() -> str:
    return '%Y-%m-%dT%H:%M%Z'


def get_current_time() -> datetime:
    return datetime.now()


def get_current_time_str() -> str:
    return get_current_time().strftime(get_datetime_format())
