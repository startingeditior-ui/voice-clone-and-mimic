"""
tests/test_transcription_fix.py — Smoke test for the Whisper transcription pipeline.

Run from the project root:
    python -m tests.test_transcription_fix

Requires a test audio file at input/recorded.wav (falls back to input/vishal.wav).
"""

import os
import sys

# Ensure the project root is on the path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.transcribe import transcribe_audio

# Prefer recorded.wav, fall back to vishal.wav
test_input = os.path.join(PROJECT_ROOT, "input", "recorded.wav")
if not os.path.exists(test_input):
    test_input = os.path.join(PROJECT_ROOT, "input", "vishal.wav")

if os.path.exists(test_input):
    print(f"Testing transcription for: {test_input}")
    try:
        text = transcribe_audio(test_input)
        print(f"✅ Transcription successful!")
        print(f"Result: {text}")
    except Exception as e:
        print(f"❌ Transcription failed: {e}")
        import traceback
        traceback.print_exc()
else:
    print(f"No test audio file found in input/. Place a WAV file at input/recorded.wav and re-run.")
