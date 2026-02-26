"""
tests/test_whisper.py — Smoke test for Faster-Whisper transcription.

Run from the project root:
    python -m tests.test_whisper

Tests CUDA loading first, falls back gracefully to CPU.
Requires a test audio file at input/recorded.wav.
"""

import os
import sys
from faster_whisper import WhisperModel

# Ensure the project root is on the path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Test audio file — prefer recorded.wav, fall back to vishal.wav
test_audio = os.path.join(PROJECT_ROOT, "input", "recorded.wav")
if not os.path.exists(test_audio):
    test_audio = os.path.join(PROJECT_ROOT, "input", "vishal.wav")

if not os.path.exists(test_audio):
    print("⚠️  No test audio found in input/. Place a WAV file at input/recorded.wav and re-run.")
    sys.exit(0)

# Try CUDA first, fall back to CPU
try:
    model = WhisperModel("base", device="cuda", compute_type="float16")
    print("✅ CUDA Whisper model loaded successfully")
except Exception as e:
    print(f"⚠️  CUDA failed ({e}), falling back to CPU...")
    model = WhisperModel("base", device="cpu", compute_type="int8")
    print("✅ CPU Whisper model loaded successfully")

print(f"Transcribing: {test_audio}")
segments, info = model.transcribe(test_audio)

print(f"Detected language: {info.language} (confidence: {info.language_probability:.2f})")
print("\nTranscription:")
for segment in segments:
    print(f"  [{segment.start:.1f}s → {segment.end:.1f}s] {segment.text.strip()}")