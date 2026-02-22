import sys
import subprocess
from transcribe import transcribe_audio
from synthesize import synthesize

print("Step 1: Recording...")
subprocess.run([sys.executable, "record_audio.py"])

input_audio = "input/recorded.wav"

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
synthesize(text, input_audio, accent=accent_choice, tone=tone_choice)

print("\n✅ Completed. Output saved at output/xtts_output.wav")