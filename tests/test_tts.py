"""
tests/test_tts.py — Standalone smoke test for XTTS v2 synthesis.

Run from the project root:
    python -m tests.test_tts

Requires a reference speaker WAV at input/recorded.wav.
The test output is saved to output/test_tts_output.wav.
"""

import os
import sys
import torch
from TTS.api import TTS

# Ensure the project root is on the path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Load XTTS v2 model
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Loading XTTS v2 on {device.upper()}...")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
tts.to(device)

# Reference speaker and output paths
speaker_wav = os.path.join(PROJECT_ROOT, "input", "recorded.wav")
output_wav  = os.path.join(PROJECT_ROOT, "output", "test_tts_output.wav")
os.makedirs(os.path.join(PROJECT_ROOT, "output"), exist_ok=True)

if not os.path.exists(speaker_wav):
    print(f"⚠️  Speaker reference not found: {speaker_wav}")
    print("   Place a short voice sample at input/recorded.wav and re-run.")
    sys.exit(0)

language = "en"
text = (
    "I am extremely excited to introduce this revolutionary AI voice system! "
    "This technology will completely transform the way we interact with machines."
)

print("Synthesising test audio...")
tts.tts_to_file(
    text=text,
    speaker_wav=speaker_wav,
    language=language,
    file_path=output_wav
)

print(f"✅ Voice generated successfully! Output: {output_wav}")
