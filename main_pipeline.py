from transcribe import transcribe_audio
from synthesize import synthesize
import sys
import subprocess

print("Step 1: Recording...")
subprocess.run([sys.executable, "record_audio.py"])

input_audio = "input/recorded.wav"

print("Step 2: Transcribing...")
text = transcribe_audio(input_audio)
if not text.strip():
    print("⚠ Warning: No speech detected. Using default text for testing.")
    text = "Hello, this is a test voice."
print("Detected Text:", text)

print("Step 3: Generating Cloned Voice...")
synthesize(text, input_audio)

print("Completed. Output saved at output/xtts_output.wav")