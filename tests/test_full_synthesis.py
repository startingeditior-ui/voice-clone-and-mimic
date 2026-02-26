"""
tests/test_full_synthesis.py — Smoke test for the full XTTS v2 synthesis pipeline.

Run from the project root:
    python -m tests.test_full_synthesis

Requires a reference WAV file at input/recorded.wav (or any other .wav).
The test synthesises a short sentence and saves it to output/test_synthesis.wav.
"""

import os
import sys

# Ensure the project root is on the path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.synthesize import synthesize

# Use a real reference wav if available; otherwise print a warning and skip.
dummy_input = os.path.join(PROJECT_ROOT, "input", "recorded.wav")
if not os.path.exists(dummy_input):
    print(f"Warning: reference file not found at {dummy_input}.")
    print("Place a short voice sample at input/recorded.wav and re-run.")
    sys.exit(0)

output_path = os.path.join(PROJECT_ROOT, "output", "test_synthesis.wav")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

try:
    print("Starting test synthesis...")
    synthesize(
        "This is a test transcription.",
        dummy_input,
        output_path=output_path
    )
    print(f"✅ Synthesis completed successfully! Output: {output_path}")
except Exception as e:
    print(f"❌ Synthesis failed: {e}")
    import traceback
    traceback.print_exc()
