from __future__ import annotations

from typing import Any

import rich
import typer

from . import __version__, _cluster, _publish, _record

app = typer.Typer()


def main() -> Any:
    return app()


@app.command()
def version() -> None:
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
    rate_in_Hz: int = typer.Option(
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
    output_file_name: str = typer.Option(
        "recording.wav",
        "--output",
        "-o",
        help="Output file name",
    ),
) -> None:
    settings = _record.RecordingSettings(
        chunk_size=chunk_size,
        sample_format=sample_format,
        channels=channels,
        rate_in_Hz=rate_in_Hz,
        recording_time_in_s=recording_time_in_s,
    )
    # TODO:
    # Change output_file_name to a output directory
    # save settings to a JSON file
    # record until the user presses Ctrl-C
    # save the recording to a set of WAV files
    # file format: <output dir>/<timestamp>_<sensor_id>.wav
    # with
    # timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%I_%M_%S_%f")
    _record.record(
        settings=settings,
        output_file_name=output_file_name,
    )


@app.command()
def cluster() -> None:
    _cluster.cluster()


@app.command()
def publish() -> None:
    _publish.publish()
