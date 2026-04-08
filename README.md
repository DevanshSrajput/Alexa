# Alexa Voice Assistant (Python)

A small Python workspace for experimenting with a voice-assistant flow (listen, parse, and respond), plus a couple of standalone CLI practice scripts.

The primary focus of this repository is the assistant implementation in [Alexa.py](Alexa.py).

## What This Project Is

- A beginner-friendly voice assistant prototype in Python.
- Built around speech recognition, text-to-speech output, and simple command handling.
- Useful as a learning sandbox for voice interfaces and Python fundamentals.

## Project Structure

- [Alexa.py](Alexa.py): Main voice-assistant script (core project file).
- [requirements.txt](requirements.txt): Python dependencies.
- [add_numbers.py](add_numbers.py): Small standalone integer-sum CLI script.
- [prime_number.py](prime_number.py): Small standalone prime-check CLI script.

## Prerequisites

- Python 3.9+
- `pip`
- Working microphone input

On macOS, voice/audio dependencies can require additional system packages for PyAudio.

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. If `pyaudio` installation fails on macOS, install PortAudio and retry:

```bash
brew install portaudio
pip install pyaudio
```

## Run

Run the assistant script:

```bash
python Alexa.py
```

If you want to run the utility scripts:

```bash
python add_numbers.py
python prime_number.py
```

## Current Status

The assistant file appears to be a work in progress and may need fixes before it runs successfully end-to-end.

Notable issues currently visible in [Alexa.py](Alexa.py):

- Typo in import name (`speech_recoginition` vs `speech_recognition`).
- Syntax issue in `engine.setProperty(...)`.
- File appears incomplete/truncated near `take_command()`.
- Typo in [requirements.txt](requirements.txt) (`pyjokesc` likely intended to be `pyjokes`).

## Suggested Next Improvements

1. Fix import and dependency typos.
2. Complete command handling flow in [Alexa.py](Alexa.py).
3. Add basic tests for helper logic.
4. Add a short command list section (supported voice commands).

## License

This project is licensed under the terms in [LICENSE](LICENSE).
