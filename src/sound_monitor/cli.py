import typer
from typing import Any
import rich

from . import (
    __version__,
    _cluster,
    _publish,
    _record,
)


app = typer.Typer()


def main() -> Any:
    return app()


@app.command()
def version() -> None:
    rich.print(f"[blue]Sounds Monitor Version[/]: [magenta]{__version__}[/]")

@app.command()
def record(
    chunk_size: int = typer.Option(_record.DEFAULT_CHUNK_SIZE, "--chunk-size", "-c", help="Chunk size to read from audio stream")
) -> None:
    _record.record()