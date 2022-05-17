# sound-monitor

[![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]
[![Code style: black][black-badge]][black-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

Package for recording, clustering and publishing sound data.

Features:
- records sound data from a microphone to a wave file (WAV) + metadata (timing, location) (`sm_record`)
- processes it to cluster similar sounds (`sm_cluster`)
- publishes the data to a specified remote storage provider (`sm_publish`)

The purpose is to study re-occuring sound events in machine rooms.

## Dependencies

This package uses `pyaudio` thus requires `portaudio19-dev` (or newer) to be installed.

## Raspberry Pi setup

```bash
    sudo apt-get install portaudio19-dev
    wget -qO- https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba
    sudo mv bin/micromamba /usr/local/bin/micromamba
```

Create python ENV
```
micromamba activate
micromamba install python=3.10 -c conda-forge
pip install sound-monitor
```

Setup services
```bash
TBD
```


<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/kreczko/sound-monitor/workflows/CI/badge.svg
[actions-link]:             https://github.com/kreczko/sound-monitor/actions
[black-badge]:              https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]:               https://github.com/psf/black
[pypi-link]:                https://pypi.org/project/sound-monitor/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/sound-monitor
[pypi-version]:             https://badge.fury.io/py/sound-monitor.svg
[rtd-badge]:                https://readthedocs.org/projects/sound-monitor/badge/?version=latest
[rtd-link]:                 https://sound-monitor.readthedocs.io/en/latest/?badge=latest
<!-- prettier-ignore-end -->

