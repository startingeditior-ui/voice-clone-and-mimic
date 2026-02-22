from TTS.api import TTS
import os

os.makedirs("output", exist_ok=True)

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

def synthesize(text, speaker_wav):
    tts.tts_to_file(
        text=text,
        speaker_wav=speaker_wav,
        language="en",
        file_path="output/xtts_output.wav"
    )