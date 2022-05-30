"""Functions for recording sound."""
from __future__ import annotations

import json
import wave
from dataclasses import asdict, dataclass

import pyaudio

DEFAULT_CHUNK_SIZE = 8192
DEFAULT_SAMPLE_FORMAT = pyaudio.paInt16  # 16 bits per sample
DEFAULT_CHANNELS = 1
DEFAULT_RATE = 44100  # Hz
DEFAULT_RECORDING_TIME = 3  # seconds


@dataclass
class RecordingSettings:
    """Settings for recording sound."""

    chunk_size: int = DEFAULT_CHUNK_SIZE
    sample_format: int = DEFAULT_SAMPLE_FORMAT
    channels: int = DEFAULT_CHANNELS
    rate_in_hz: int = DEFAULT_RATE
    recording_time_in_s: int = DEFAULT_RECORDING_TIME

    def to_json(self) -> str:
        """Convert settings to JSON."""
        return json.dumps(asdict(self))


def _save_to_wave(
    settings: RecordingSettings,
    sample_size: int,
    output_file_name: str,
    frames: list[bytes],
) -> None:
    """Save recorded data to a wave file."""
    # Save the recorded data as a WAV file
    print(f"Saving file {output_file_name}")
    wave_file = wave.open(output_file_name, "wb")
    wave_file.setnchannels(settings.channels)
    wave_file.setsampwidth(sample_size)
    wave_file.setframerate(settings.rate_in_hz)
    wave_file.writeframes(b"".join(frames))
    wave_file.close()


def record(
    settings: RecordingSettings,
    output_file_name: str = "recording.wav",
) -> None:
    """Record sound."""
    port_audio = pyaudio.PyAudio()  # Create an interface to PortAudio
    print(f"Starting recording of {output_file_name}")
    stream = port_audio.open(
        format=settings.sample_format,
        channels=settings.channels,
        rate=settings.rate_in_hz,
        frames_per_buffer=settings.chunk_size,
        input=True,
        output=False,
    )

    frames: list[bytes] = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for _ in range(
        0, int(settings.rate_in_hz / settings.chunk_size * settings.recording_time_in_s)
    ):
        data = stream.read(settings.chunk_size)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    port_audio.terminate()

    print(f"Finished recording of {output_file_name}")
    _save_to_wave(
        settings=settings,
        sample_size=port_audio.get_sample_size(settings.sample_format),
        output_file_name=output_file_name,
        frames=frames,
    )
