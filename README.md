# Audio2Text

A powerful tool for converting audio content to text with timestamps, specifically designed for processing YouTube videos and audio files.

## Features

- YouTube video audio download and conversion
- High-quality speech-to-text transcription using NVIDIA's Parakeet model
- Timestamp generation for words, segments, and characters
- SRT subtitle file generation
- Clean text output
- Batch processing support
- Progress tracking with tqdm

## Important Notice

This project uses NVIDIA's Parakeet model (tdt-0.6b-v2) which is **strictly limited to English educational purposes only**. The model is sourced from [NVIDIA's Hugging Face Space](https://huggingface.co/spaces/nvidia/parakeet-tdt-0.6b-v2).

### Usage Restrictions
- Only for English language content
- Limited to educational purposes
- Not for commercial use
- Not for general speech recognition tasks
- Not for non-English content
- We're working to make this project a real-time transcription

## Project Structure

```
Audio2Text/
├── Audio/             # Directory for storing audio files
├── Clean_Text/        # Directory for storing clean text transcriptions
├── Script/            # Directory for storing SRT subtitle files
├── Urls/              # Directory for storing URL lists
├── download_yt.py     # YouTube audio downloader
├── test_mul.py        # Main transcription script
└── test.py            # Test script
```

## Prerequisites

- Python 3.7+
- NVIDIA GPU (recommended for faster processing)
- Required Python packages:
  - nemo
  - librosa
  - pytubefix
  - pydub
  - polars
  - tqdm
  - others please check nvidia/parakeet-tdt-0.6b-v2 official web

## Installation

1. Clone the repository
2. Install the required packages (uv is highly recommend):
```bash
uv pip install nemo-toolkit[all] librosa pytubefix pydub polars tqdm
```

## Usage

### 1. Downloading YouTube Audio

1. Create a CSV file in the `Urls` directory with a column named "URL" containing YouTube video URLs
2. Run the download script:
```bash
python download_yt.py
```

### 2. Transcribing Audio

1. Place your audio files in the `Audio` directory
2. Run the transcription script:
```bash
python test_mul.py
```

The script will:
- Process all audio files in the `Audio` directory
- Generate SRT subtitle files in the `Script` directory
- Create clean text transcriptions in the `Clean_Text` directory
- Display progress and timing information

## Output Files

- **SRT Files**: Located in the `Script` directory, containing timestamped transcriptions
- **Clean Text**: Located in the `Clean_Text` directory, containing plain text transcriptions
- **Audio Files**: Stored in the `Audio` directory

## Performance

The transcription process uses NVIDIA's Parakeet model (tdt-0.6b-v2) for high-quality speech recognition. Processing time depends on:
- Audio file length
- Hardware specifications
- Number of files being processed

### Model Limitations
- Optimized for English educational content
- May not perform well on:
  - Non-English audio
  - Noisy environments
  - Multiple speakers
  - Non-educational content
  - Commercial applications

## Notes

- The system processes audio in chunks of 720 seconds (12 minutes) by default, It depends on your GPU performance
- Audio is automatically resampled to 16kHz for optimal transcription quality
- Progress bars show real-time processing status
- Total processing time and audio duration are displayed upon completion
- Please ensure all processed content is English educational material only

## License

MIT License

Copyright (c) 2025 Cheng Lin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contributing

