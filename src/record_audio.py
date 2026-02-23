"""
record_audio.py — Records a 10-second audio clip from the microphone.

Run from the project root:
    python -m src.record_audio
"""

import sounddevice as sd
from scipy.io.wavfile import write
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_DIR = os.path.join(PROJECT_ROOT, "input")
os.makedirs(INPUT_DIR, exist_ok=True)

fs = 16000
seconds = 10

print("Recording...")
audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

output_path = os.path.join(INPUT_DIR, "recorded.wav")
write(output_path, fs, audio)
print(f"Saved to {output_path}")