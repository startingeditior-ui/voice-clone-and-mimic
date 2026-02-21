import librosa
import soundfile as sf
import noisereduce as nr
import numpy as np

# Load
y, sr = librosa.load("sneha.wav", sr=22050)

# Trim silence
y_trimmed, _ = librosa.effects.trim(y, top_db=25)

# Noise reduction
reduced = nr.reduce_noise(y=y_trimmed, sr=sr)

# Normalize
reduced = reduced / np.max(np.abs(reduced))

sf.write("clear.wav", reduced, sr)

print("Cleaned speaker saved.")
