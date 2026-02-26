"""
tests/test_voice.py — Manual audio-cleaning utility (scratch test).

This is a one-off helper that loads a speaker WAV, applies noise reduction,
trims silence, and normalises it — saving the result as a "clean" reference
for use with XTTS v2.

Run from the project root:
    python -m tests.test_voice

Place your source audio at input/speaker_raw.wav (or update INPUT_WAV below).
Output is saved to input/speaker_clean.wav.
"""

import os
import sys
import librosa
import soundfile as sf
import noisereduce as nr
import numpy as np

# Ensure the project root is on the path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

INPUT_WAV  = os.path.join(PROJECT_ROOT, "input", "speaker_raw.wav")
OUTPUT_WAV = os.path.join(PROJECT_ROOT, "input", "speaker_clean.wav")

if not os.path.exists(INPUT_WAV):
    print(f"⚠️  Input file not found: {INPUT_WAV}")
    print("   Place your raw speaker audio at input/speaker_raw.wav and re-run.")
    sys.exit(0)

print(f"Loading {INPUT_WAV}...")
y, sr = librosa.load(INPUT_WAV, sr=22050)

# Trim leading/trailing silence
y_trimmed, _ = librosa.effects.trim(y, top_db=25)

# Spectral-subtraction noise reduction
print("Applying noise reduction...")
reduced = nr.reduce_noise(y=y_trimmed, sr=sr)

# Peak normalise to prevent clipping
reduced = reduced / np.max(np.abs(reduced))

sf.write(OUTPUT_WAV, reduced, sr)
print(f"✅ Cleaned speaker audio saved to: {OUTPUT_WAV}")
