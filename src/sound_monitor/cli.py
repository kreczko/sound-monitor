"""Command line interface for the sound monitor."""
from __future__ import annotations

import os
import socket
from typing import Any

import rich
import typer

from . import __version__, _cluster, _date, _publish, _record
from ._logger import logger

app = typer.Typer()


def main() -> Any:
    """Main function."""
    return app()


@app.command()
def version() -> None:
    """Print the version number."""
    rich.print(f"[blue]Sounds Monitor Version[/]: [magenta]{__version__}[/]")


@app.command()
def record(
    chunk_size: int = typer.Option(
        _record.DEFAULT_CHUNK_SIZE,
        "--chunk-size",
        "-c",
        help="Chunk size to read from audio stream",
    ),
    sample_format: int = typer.Option(
        _record.DEFAULT_SAMPLE_FORMAT,
        "--sample-format",
        "-s",
        help="Sample format to use",
    ),
    channels: int = typer.Option(
        _record.DEFAULT_CHANNELS,
        "--channels",
        "-n",
        help="Number of channels to use",
    ),
    rate_in_hz: int = typer.Option(
        _record.DEFAULT_RATE,
        "--rate",
        "-r",
        help="Sample rate to use",
    ),
    recording_time_in_s: int = typer.Option(
        _record.DEFAULT_RECORDING_TIME,
        "--recording-time",
        "-t",
        help="Recording time in seconds",
    ),
    number_of_recordings: int = typer.Option(
        1,
        "--number-of-recordings",
        "-p",
        help="number of recordings",
    ),
    output_folder: str = typer.Option(
        "/tmp",
        "--output",
        "-o",
        help="Output file name",
    ),
    device_index: int = typer.Option(
        _record.DEFAULT_DEVICE_INDEX,
        "--device-index",
        "-d",
        help="Device index to use",
    ),
) -> None:
    """Record sound."""
    settings = _record.RecordingSettings(
        chunk_size=chunk_size,
        sample_format=sample_format,
        channels=channels,
        rate_in_hz=rate_in_hz,
        recording_time_in_s=recording_time_in_s,
        device_index=device_index,
        output_folder=output_folder,
        number_of_recordings=number_of_recordings,
    )
    json_file = os.path.join(output_folder, "settings.json")
    with open(json_file, "w") as f:
        f.write(settings.to_json())
    # TODO:
    # record until the user presses Ctrl-C
    # save the recording to a set of WAV files
    # file format: <output dir>/<timestamp>_<sensor_id>.wav
    sensor_id = socket.gethostname()
    for n in range(settings.number_of_recordings):
        logger.info(f"Recording #{n} on {sensor_id}")
        timestamp = _date.current_formatted_date()
        output_file_name = f"{timestamp}_{sensor_id}.wav"
        output_file_name = os.path.join(settings.output_folder, output_file_name)
        _record.record(
            settings=settings,
            output_file_name=output_file_name,
        )


@app.command()
def cluster() -> None:
    """Cluster sounds data into sound events."""
    _cluster.cluster()


@app.command()
def publish() -> None:
    """Publish sound events to one or more platform."""
    _publish.publish()
