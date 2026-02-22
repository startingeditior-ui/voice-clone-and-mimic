import librosa
import soundfile as sf
import noisereduce as nr
import numpy as np


y, sr = librosa.load("sneha.wav", sr=22050)


y_trimmed, _ = librosa.effects.trim(y, top_db=25)


reduced = nr.reduce_noise(y=y_trimmed, sr=sr)


reduced = reduced / np.max(np.abs(reduced))

sf.write("clear.wav", reduced, sr)

print("Cleaned speaker saved.")
