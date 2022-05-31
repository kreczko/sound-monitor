"""Logging module for soundmon"""
from __future__ import annotations

import logging

from rich.logging import RichHandler

from . import _date


class LevelFormatter(logging.Formatter):
    """
    From https://stackoverflow.com/a/28636024/362457
    """

    def __init__(self, fmt: str, datefmt: str, level_fmts: dict[int, str]):
        self._level_formatters = {}
        for level, format_str in level_fmts.items():
            # Could optionally support level names too
            self._level_formatters[level] = logging.Formatter(
                fmt=format_str, datefmt=datefmt
            )
        # self._fmt will be the default format
        super().__init__(fmt=fmt, datefmt=datefmt)

    def format(self, record: logging.LogRecord) -> str:
        if record.levelno in self._level_formatters:
            return self._level_formatters[record.levelno].format(record)

        return super().format(record)


logger = logging.getLogger("soundmon")
logger.setLevel(logging.INFO)

console_formatter = LevelFormatter(
    fmt="%(asctime)s [%(name)s]  %(levelname)s: %(message)s",
    datefmt=f"[{_date.DEFAULT_DATE_FORMAT} {_date.DEFAULT_TIME_FORMAT}]",
    level_fmts={
        logging.INFO: "%(message)s",
        logging.WARNING: "[bold dark_orange]%(levelname)s[/]: %(message)s",
        logging.ERROR: "[bold red]%(levelname)s[/]: %(message)s",
        logging.DEBUG: "[bold hot_pink]%(levelname)s[/]: %(message)s",
        logging.CRITICAL: "[bold blink bright_red]%(levelname)s[/]: %(message)s",
    },
)
console_handler = RichHandler(
    # rich_tracebacks=True, # does not work with custom formatters
    markup=True,
    show_level=False,
    show_time=False,
    show_path=False,
)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(console_formatter)
console_handler.formatter = console_formatter

logfile_formatter = logging.Formatter(
    "%(asctime)s [%(name)s]  %(levelname)s: %(message)s"
)
logfile_handler = logging.FileHandler(
    f"/tmp/{_date.current_formatted_date()}_soundmon.log"
)
logfile_handler.setLevel(logging.DEBUG)
logfile_handler.setFormatter(logfile_formatter)

logger.addHandler(console_handler)
logger.addHandler(logfile_handler)
