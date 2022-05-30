import datetime

DEFAULT_DATE_FORMAT = "%Y_%m_%d_T%H_%M_%S_%f"

def current_formatted_date() -> str:
    """Return the current date formatted as ISO 8601."""
    return datetime.datetime.now().strftime(DEFAULT_DATE_FORMAT)