from faster_whisper import WhisperModel

try:
    model = WhisperModel("base", device="cuda", compute_type="float16")
    print("CUDA loaded successfully")
except Exception as e:
    print("CUDA failed:", e)

segments, info = model.transcribe("vishal.wav")

for segment in segments:
    print(segment.text)