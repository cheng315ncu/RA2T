# Real-time Speech-to-Text Application

This application provides real-time speech-to-text functionality using NVIDIA's NeMo ASR model. It captures audio from your microphone and transcribes it in real-time.

## Model Information

This project uses the NVIDIA Parakeet TDT 0.6B V2 model from Hugging Face:
- Source: [nvidia/parakeet-tdt-0.6b-v2](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2)
- Model Architecture: FastConformer-TDT
- Model Size: 600 million parameters
- Features:
  - Accurate word-level timestamp predictions
  - Automatic punctuation and capitalization
  - Robust performance on spoken numbers and song lyrics transcription

**License Note**: The model is governed by the CC-BY-4.0 license. While this model is available for commercial use, this specific project implementation is restricted to educational and personal purposes only.

## Usage Restrictions

This project is specifically designed for:
- NCU EMI (English as a Medium of Instruction) courses
- Real-time English subtitles generation
- Post-class transcription generation
- Educational purposes
- Personal use

**Important**: This project is NOT intended for commercial use. Any commercial application or distribution is strictly prohibited.

## Prerequisites

- Python 3.8 or higher
- Windows 10/11 (This application does not work in WSL)
- A working microphone
- NVIDIA GPU (recommended for better performance, I don't have a mac, but huggingface has model for mlx (Apple Silicon solution), you can adjust base on this project)

## Why Not WSL?

This application cannot run in WSL (Windows Subsystem for Linux) due to several limitations:

1. **Audio Device Access**: WSL has limited access to Windows audio devices, making it difficult to capture real-time audio input.
2. **CUDA Support**: While WSL2 supports CUDA, the audio device handling in WSL is not as robust as native Windows.
3. **SoundDevice Library**: The `sounddevice` library used in this project has known issues with WSL's audio subsystem.

## Environment Setup

### 1. Install uv

First, install `uv`, a fast Python package installer and resolver:

```bash
pip install uv
```

### 2. Create and Activate Virtual Environment

```bash
# Create a new virtual environment
uv venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install dependencies using uv
uv pip install -r requirements.txt
```

## Usage

1. Make sure your microphone is properly connected and set as the default input device.

2. Run the application:
```bash
python A2T.py
```

3. Start speaking into your microphone. The application will transcribe your speech in real-time.

4. Press `Ctrl+C` to stop the application.

## Features

- Real-time speech-to-text conversion (show on terminal, we're working to display over screen)
- Automatic audio buffering and processing (adjust seconds for buffering base on speaker's habit)
- Clean console output showing only transcription results (verbose = False)
- Support for continuous speech recognition

## Troubleshooting

### Common Issues

1. **No Audio Input**
   - Check if your microphone is properly connected
   - Verify that the microphone is set as the default input device
   - Ensure the application has permission to access the microphone

2. **CUDA/GPU Issues**
   - Make sure you have the proper NVIDIA drivers installed
   - Verify CUDA installation if using GPU acceleration

3. **Performance Issues**
   - The application works best with an NVIDIA GPU
   - CPU-only mode may be slower

## Dependencies

- numpy>=1.21.0
- sounddevice>=0.4.5
- nemo-toolkit[asr]>=1.20.0
- torch>=2.0.0

## License

This project is licensed under the MIT License - see the LICENSE file for details.

**Note**: While this project is under MIT License, its usage is restricted to educational and personal purposes only. Commercial use is not permitted. The underlying ASR model (Parakeet TDT 0.6B V2) is governed by the CC-BY-4.0 license.

## Acknowledgments

- NVIDIA NeMo team for the ASR model
- Cheng Lin from BorgLab NCU
