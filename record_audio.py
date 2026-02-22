import sounddevice as sd
from scipy.io.wavfile import write
import os

os.makedirs("input", exist_ok=True)

fs = 16000
seconds = 10

print("Recording...")
audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

write("input/recorded.wav", fs, audio)
print("Saved to input/recorded.wav")