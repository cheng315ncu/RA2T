import sounddevice as sd
import numpy as np
import nemo.collections.asr as nemo_asr
from nemo.utils import logging as nemo_logging
import queue
import threading
import time
import contextlib
import sys
import os

# Set NeMo logging level
nemo_logging.set_verbosity(nemo_logging.CRITICAL)

# Initialize ASR model
asr_model = nemo_asr.models.ASRModel.from_pretrained(model_name="nvidia/parakeet-tdt-0.6b-v2")

# Audio parameters
SAMPLE_RATE = 16000  # Sampling rate
CHANNELS = 1         # Mono channel
CHUNK_SIZE = 1024    # Audio chunk size
BUFFER_SIZE = 5      # Buffer size (seconds)

# Create audio buffer
audio_queue = queue.Queue()
is_recording = True

@contextlib.contextmanager
def suppress_stdout():
    """Temporarily suppress standard output"""
    stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    try:
        yield
    finally:
        sys.stdout = stdout

def audio_callback(indata, frames, time, status):
    """Audio callback function, stores microphone input in buffer"""
    if status:
        print(f"Audio input status: {status}")
    audio_queue.put(indata.copy())

def process_audio():
    """Process audio and perform transcription"""
    buffer = []
    last_process_time = time.time()
    
    while is_recording:
        try:
            # Get audio data from buffer
            audio_chunk = audio_queue.get(timeout=1)
            buffer.extend(audio_chunk.flatten())
            
            # Process audio every 3 seconds
            current_time = time.time()
            if current_time - last_process_time >= 3 and len(buffer) > 0:
                # Convert buffer to numpy array
                audio_data = np.array(buffer)
                
                # Use context manager to suppress transcription progress bar
                with suppress_stdout():
                    # Perform transcription
                    output = asr_model.transcribe([audio_data], timestamps=True, batch_size=1, verbose=False)
                
                # Only show transcription results
                if output[0].timestamp['segment']:
                    for segment in output[0].timestamp['segment']:
                        print(segment['segment'])
                
                # Clear buffer
                buffer = []
                last_process_time = current_time
                
        except queue.Empty:
            continue
        except Exception as e:
            print(f"Error processing audio: {e}")

def main():
    global is_recording
    
    print("Recording started, press Ctrl+C to stop...")
    is_recording = True
    
    # Start audio processing thread
    process_thread = threading.Thread(target=process_audio)
    process_thread.start()
    
    try:
        # Start recording
        with sd.InputStream(callback=audio_callback,
                          channels=CHANNELS,
                          samplerate=SAMPLE_RATE,
                          blocksize=CHUNK_SIZE):
            while is_recording:
                time.sleep(0.05)
                
    except KeyboardInterrupt:
        print("\nStopping recording...")
        is_recording = False
        process_thread.join()

if __name__ == "__main__":
    main()
