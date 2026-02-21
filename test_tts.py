import torch
from TTS.api import TTS

# Load XTTS v2 model
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

# Device selection
device = "cuda" if torch.cuda.is_available() else "cpu"
tts.to(device)

# ====== CONFIGURATION ======
speaker_wav = "clear.wav"   # 5–15 sec clean voice sample
language = "en"

# ====== TONE MODIFIED TEXT ======
text = """
I am extremely excited to introduce this revolutionary AI voice system!
This technology will completely transform the way we interact with machines. lot more difficult
"""

# Generate with tone tuning
tts.tts_to_file(
    text=text,
    speaker_wav=speaker_wav,
    language=language,
    file_path="output.wav"
)

print("Voice generated successfully!")
