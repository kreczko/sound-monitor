from __future__ import annotations

import datetime

DEFAULT_TIMESTAMP_FORMAT = "%Y_%m_%d_T%H_%M_%S_%f"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
DEFAULT_TIME_FORMAT = "%H:%M:%S"


def current_formatted_date() -> str:
    """Return the current date formatted as ISO 8601."""
    return datetime.datetime.now().strftime(DEFAULT_TIMESTAMP_FORMAT)
