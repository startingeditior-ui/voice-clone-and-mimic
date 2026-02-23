import os
from TTS.api import TTS

# Workaround for lazy-loading ModuleNotFoundError in some environments
try:
    from transformers import GenerationMixin, GPT2PreTrainedModel
    print("Pre-loaded transformers in synthesize module.")
except ImportError:
    pass

# Resolve output directory relative to project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

ACCENTS = {
    "neutral": "en",
    "american": "en",
    "british": "en",
    "indian": "en"
}

TONES = ["calm", "energetic", "dramatic"]

def synthesize(text, speaker_wav, accent="neutral", tone="calm", output_path=None):
    if output_path is None:
        output_path = os.path.join(OUTPUT_DIR, "xtts_output.wav")

    language_code = ACCENTS.get(accent.lower(), "en")
    if accent.lower() == "indian":
        print("⚠ Indian English accent not natively supported, using neutral English.")

    if tone.lower() not in TONES:
        print(f"⚠ Tone '{tone}' not recognized, using 'calm'.")
        tone = "calm"

    print(f"Generating voice with accent={accent}, tone={tone} to {output_path}...")

    tts.tts_to_file(
        text=text,
        speaker_wav=speaker_wav,
        language=language_code,
        file_path=output_path
    )
    print(f"✅ Voice generated successfully at {output_path}")