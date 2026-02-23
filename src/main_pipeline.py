"""
main_pipeline.py — CLI pipeline for the Voice Clone project.

Run from the project root:
    python -m src.main_pipeline
"""

import sys
import subprocess
import os

# Ensure project root is on path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.transcribe import transcribe_audio
from src.synthesize import synthesize

print("Step 1: Recording...")
subprocess.run([sys.executable, "-m", "src.record_audio"])

input_audio = os.path.join(PROJECT_ROOT, "input", "recorded.wav")

print("Step 2: Transcribing...")
text = transcribe_audio(input_audio)
if not text.strip():
    text = "Hello, this is a test voice."

print("Detected Text:", text)

print("\nChoose Accent: neutral, american, british, indian")
accent_choice = input("Accent: ").strip().lower()
if accent_choice not in ["neutral", "american", "british", "indian"]:
    print("Invalid choice, using neutral accent.")
    accent_choice = "neutral"

print("\nChoose Tone: calm, energetic, dramatic")
tone_choice = input("Tone: ").strip().lower()
if tone_choice not in ["calm", "energetic", "dramatic"]:
    print("Invalid choice, using calm tone.")
    tone_choice = "calm"

print(f"\nStep 3: Generating Cloned Voice with accent={accent_choice} & tone={tone_choice}...")
output_path = os.path.join(PROJECT_ROOT, "output", "xtts_output.wav")
synthesize(text, input_audio, accent=accent_choice, tone=tone_choice, output_path=output_path)

print(f"\n✅ Completed. Output saved at {output_path}")