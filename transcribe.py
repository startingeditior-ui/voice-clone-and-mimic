from faster_whisper import WhisperModel

model = WhisperModel("base", device="cuda", compute_type="float16")

def transcribe_audio(path):
    segments, info = model.transcribe(path)
    text = ""
    for segment in segments:
        text += segment.text + " "
    return text.strip()