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
    chunk_size: int
    | None = typer.Option(
        _record.DEFAULT_CHUNK_SIZE,
        "--chunk-size",
        "-c",
        help="Chunk size to read from audio stream",
    ),
) -> None:
    _record.record()


@app.command()
def cluster() -> None:
    _cluster.cluster()


@app.command()
def publish() -> None:
    _publish.publish()
