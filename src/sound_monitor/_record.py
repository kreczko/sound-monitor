from __future__ import annotations

import json
from dataclasses import asdict, dataclass

import pyaudio
import wave

DEFAULT_CHUNK_SIZE = 8192
DEFAULT_SAMPLE_FORMAT = pyaudio.paInt16  # 16 bits per sample
DEFAULT_CHANNELS = 1
DEFAULT_RATE = 44100  # Hz
DEFAULT_RECORDING_TIME = 3  # seconds


@dataclass
class RecordingSettings:
    chunk_size: int = DEFAULT_CHUNK_SIZE
    sample_format: int = DEFAULT_SAMPLE_FORMAT
    channels: int = DEFAULT_CHANNELS
    rate_in_Hz: int = DEFAULT_RATE
    recording_time_in_s: int = DEFAULT_RECORDING_TIME

    def to_json(self) -> str:
        return json.dumps(asdict(self))


def _save_to_wave(
    settings: RecordingSettings,
    sample_size: int,
    output_file_name: str,
    frames: list[bytes],
) -> None:
    # Save the recorded data as a WAV file
    wf = wave.open(output_file_name, "wb")
    wf.setnchannels(settings.channels)
    wf.setsampwidth(sample_size)
    wf.setframerate(settings.rate_in_Hz)
    wf.writeframes(b"".join(frames))
    wf.close()


def record(
    settings: RecordingSettings,
    output_file_name: str = "recording.wav",
) -> None:

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    stream = p.open(
        format=settings.sample_format,
        channels=settings.channels,
        rate=settings.rate_in_Hz,
        frames_per_buffer=settings.chunk_size,
        input=True,
    )

    frames: list[bytes] = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for _ in range(
        0, int(settings.rate_in_Hz / settings.chunk_size * settings.recording_time_in_s)
    ):
        data = stream.read(settings.chunk_size)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    # print("Finished recording")
    _save_to_wave(
        settings=settings,
        sample_size=p.get_sample_size(settings.sample_format),
        output_file_name=output_file_name,
        frames=frames,
    )
