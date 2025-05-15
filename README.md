# Real-time Speech-to-Text Transcription

This project implements real-time speech-to-text transcription using NVIDIA's Parakeet TDT 0.6B V2 model. It captures audio from your microphone and provides continuous transcription with a sliding window approach.

## Features

- Real-time audio capture and transcription
- Sliding window processing for continuous transcription
- Timestamp support for each transcribed segment
- Efficient audio buffering and processing
- Suppressed progress bars for cleaner output

## Prerequisites

- Python 3.8 or higher
- A microphone
- NVIDIA GPU (recommended for better performance)

## Installation

1. Install `uv` (Python package installer and virtual environment manager):
```bash
pip install uv
```

2. Create and activate a virtual environment using `uv`:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the required packages:
```bash
uv pip install -r requirements.txt
```

## Why Use `uv`?

`uv` is a modern Python package installer and virtual environment manager that offers several advantages:
- Faster package installation compared to pip
- Built-in virtual environment management
- Better dependency resolution
- Improved caching mechanisms
- Native support for modern Python packaging standards

## Usage

1. Run the script:
```bash
python A2T.py
```

2. Start speaking into your microphone. The transcription will appear in real-time.

3. Press `Ctrl+C` to stop the recording and transcription.

## Model Information

This project uses the [NVIDIA Parakeet TDT 0.6B V2](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2) model, which is a state-of-the-art automatic speech recognition model. Key features of the model include:

- 600M parameter FastConformer architecture
- Support for punctuation and capitalization
- Accurate timestamp predictions
- Robust performance on various audio conditions

## Configuration

You can modify the following parameters in the script:

- `SAMPLE_RATE`: Audio sampling rate (default: 16000 Hz)
- `CHANNELS`: Number of audio channels (default: 1 for mono)
- `CHUNK_SIZE`: Size of audio chunks (default: 1024)
- `WINDOW_SIZE`: Size of the sliding window in seconds (default: 3)
- `OVERLAP`: Overlap between windows in seconds (default: 1)

## Requirements

Create a `requirements.txt` file with the following dependencies:

```
sounddevice
numpy
nemo_toolkit[asr]
```

## License

This project uses the NVIDIA Parakeet TDT 0.6B V2 model, which is licensed under the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) license.

## Acknowledgments

- [NVIDIA NeMo](https://github.com/NVIDIA/NeMo) for the ASR toolkit
- [NVIDIA Parakeet TDT 0.6B V2](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2) for the speech recognition model 
