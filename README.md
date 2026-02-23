# Voice Clone Project

A FastAPI-powered voice cloning application that can:
- **Clone a voice** from an uploaded audio sample using XTTS v2 (Text-to-Speech)
- **Mimic accent & tone** using Speech-to-Speech conversion via [Retrieval-based Voice Conversion (RVC)](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

---

## 📁 Project Structure

```
Voice-clone-project/
├── src/                    # Backend Python source code
│   ├── app.py              # FastAPI application (main entry point)
│   ├── transcribe.py       # Whisper-based audio transcription
│   ├── synthesize.py       # XTTS v2 voice synthesis
│   ├── rvc_wrapper.py      # RVC voice conversion wrapper
│   ├── record_audio.py     # Microphone recording utility
│   └── main_pipeline.py    # CLI pipeline (record → transcribe → synthesize)
├── frontend/               # Web UI
│   └── index.html
├── tests/                  # Test scripts
│   ├── test_tts.py
│   ├── test_voice.py
│   ├── test_whisper.py
│   ├── test_rvc_env.py
│   ├── test_full_synthesis.py
│   └── test_transcription_fix.py
├── scripts/                # Helper scripts
│   └── start_server.bat    # Windows launcher for the FastAPI server
├── input/                  # Uploaded audio files (gitignored)
├── output/                 # Generated audio files (gitignored)
├── requirements.txt        # Main environment dependencies
├── requirements-rvc.txt    # RVC environment dependencies
└── .gitignore
```

> **Note:** `Retrieval-based-Voice-Conversion-WebUI/` and `YourTTS/` must be cloned separately (see Setup).

---

## ⚙️ Setup

### Prerequisites
- Python 3.10+
- [ffmpeg](https://ffmpeg.org/download.html) (must be on your `PATH`)
- Git

### 1. Clone the repository
```bash
git clone https://github.com/your-username/voice-clone-project.git
cd voice-clone-project
```

### 2. Create the main virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

### 3. Set up the RVC environment (for Mimicry Mode)
```bash
python -m venv rvc_env
rvc_env\Scripts\activate

pip install -r requirements-rvc.txt
```

### 4. Clone external dependencies
```bash
# RVC WebUI (required for Mimicry Mode)
git clone https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI.git

# Download required RVC assets (rmvpe, hubert, etc.) per RVC docs
```

---

## 🚀 Running the Application

### Option A — Windows batch script
```
scripts\start_server.bat
```

### Option B — Manual
```bash
# From project root, with venv active:
python -m src.app
```

Then open your browser at: **http://localhost:8000**

---

## 🎛️ Features

### Mode 1 — Voice Clone (TTS)
Upload a reference audio clip. The app will:
1. Transcribe the audio (or use your custom text)
2. Synthesize it in the cloned voice using XTTS v2

### Mode 2 — Mimicry (Speech-to-Speech)
Upload a **performance audio** (accent/tone you want) and a **target voice** file. The app uses RVC to convert the performance audio to sound like the target voice, preserving the original accent and tone.

> Requires a trained `.pth` RVC model placed in `Retrieval-based-Voice-Conversion-WebUI/assets/weights/`.

---

## 🧪 Running Tests

Run individual tests from the project root:
```bash
python -m tests.test_tts
python -m tests.test_whisper
python -m tests.test_rvc_env
```

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `fastapi` | Web API framework |
| `uvicorn` | ASGI server |
| `TTS` (Coqui) | XTTS v2 voice synthesis |
| `faster-whisper` | Audio transcription |
| `torch` | Deep learning backend |
| `sounddevice` / `scipy` | Audio recording |
| `soundfile` | Audio file I/O |

---

## 🗒️ Notes

- Audio files in `input/` and `output/` are **gitignored** — they will not be pushed to GitHub.
- Model weights (`.pth`, `.bin`, `.pt`) are also gitignored due to file size.
- The RVC and YourTTS repos are external dependencies — clone them separately as described above.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
