"""
main_pipeline.py — CLI pipeline for the Voice Clone project.

Run from the project root:
    python -m src.main_pipeline

This is a simple interactive CLI that:
  1. Records audio from the microphone
  2. Transcribes it via Whisper
  3. Lets you pick an accent and tone
  4. Synthesises the cloned voice using XTTS v2
"""

import sys
import subprocess
import os

# Ensure project root is on path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.transcribe import transcribe_audio
from src.synthesize import synthesize, ACCENTS, TONES

print("Step 1: Recording...")
subprocess.run([sys.executable, "-m", "src.record_audio"])

input_audio = os.path.join(PROJECT_ROOT, "input", "recorded.wav")

print("Step 2: Transcribing...")
text = transcribe_audio(input_audio)
if not text.strip():
    text = "Hello, this is a test voice."

print("Detected Text:", text)

# Show all supported accents
accent_choices = list(ACCENTS.keys())
print(f"\nChoose Accent: {', '.join(accent_choices)}")
accent_choice = input("Accent: ").strip().lower()
if accent_choice not in accent_choices:
    print(f"Invalid choice, using 'neutral' accent.")
    accent_choice = "neutral"

# Show all supported tones
print(f"\nChoose Tone: {', '.join(TONES)}")
tone_choice = input("Tone: ").strip().lower()
if tone_choice not in TONES:
    print(f"Invalid choice, using 'calm' tone.")
    tone_choice = "calm"

print(f"\nStep 3: Generating Cloned Voice with accent={accent_choice} & tone={tone_choice}...")
output_path = os.path.join(PROJECT_ROOT, "output", "xtts_output.wav")
synthesize(text, input_audio, accent=accent_choice, tone=tone_choice, output_path=output_path)

print(f"\n✅ Completed. Output saved at {output_path}")