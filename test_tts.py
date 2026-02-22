import torch
from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

device = "cuda" if torch.cuda.is_available() else "cpu"
tts.to(device)


speaker_wav = "clear.wav"   
language = "en"


text = """
I am extremely excited to introduce this revolutionary AI voice system!
This technology will completely transform the way we interact with machines. lot more difficult
"""

tts.tts_to_file(
    text=text,
    speaker_wav=speaker_wav,
    language=language,
    file_path="output.wav"
)

print("Voice generated successfully!")
