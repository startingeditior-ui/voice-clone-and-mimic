# 🎙️ Voice Clone Project

A **FastAPI-powered voice cloning application** that clones any voice from a short audio sample using state-of-the-art AI models — XTTS v2 for synthesis and Faster-Whisper for transcription.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-green)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 🚀 Features

| Mode | Description |
|------|-------------|
| **TTS Clone** | Upload a voice sample → transcribe (or type custom text) → synthesise in that voice |
| **Smart Mimic** | Upload a target voice + performance audio → transcribe + re-synthesise with target voice |
| **RVC Mimic** | Upload a performance audio + RVC model → convert voice while preserving accent & tone |

- 🌍 **14 languages & accents** (English, Spanish, French, German, Hindi, Japanese, Korean, Chinese, Arabic, and more)
- 🎭 **5 tone styles** — calm, energetic, dramatic, whisper, cheerful
- 🎛️ **Adjustable speech speed** (0.8×–1.2×)
- 🔊 **Automatic audio pre/post-processing** — noise reduction, high-pass filter, normalisation
- 🐳 **Docker-ready** with GPU support (NVIDIA CUDA 12.1)

---

## 📁 Project Structure

```
Voice-clone-project/
├── src/                         # Backend Python source
│   ├── app.py                   # FastAPI application (main entry point)
│   ├── transcribe.py            # Faster-Whisper audio transcription
│   ├── synthesize.py            # XTTS v2 voice synthesis (TTS Clone + Smart Mimic)
│   ├── audio_processor.py       # Pre/post-processing (denoise, filter, normalise)
│   ├── rvc_wrapper.py           # RVC voice conversion wrapper
│   ├── record_audio.py          # Microphone recording utility
│   └── main_pipeline.py         # CLI pipeline (record → transcribe → synthesize)
├── frontend/
│   └── index.html               # Single-page web UI
├── tests/
│   ├── test_audio_processor.py  # Unit tests for audio preprocessing
│   ├── test_tts.py              # XTTS v2 standalone smoke test
│   ├── test_whisper.py          # Faster-Whisper standalone smoke test
│   ├── test_voice.py            # Audio-cleaning utility (raw → clean WAV)
│   ├── test_rvc_env.py          # RVC environment smoke test
│   ├── test_full_synthesis.py   # End-to-end synthesis smoke test
│   └── test_transcription_fix.py# Transcription pipeline smoke test
├── scripts/
│   └── start_server.bat         # Windows launcher for the FastAPI server
├── input/                       # Uploaded audio files (gitignored)
├── output/                      # Generated audio files (gitignored)
├── Dockerfile                   # Docker image definition (CUDA 12.1 + Ubuntu 22.04)
├── docker-compose.yml           # Docker Compose with GPU support & volume mounts
├── .dockerignore                # Files excluded from Docker build context
├── requirements.txt             # Main environment dependencies
├── requirements-rvc.txt         # RVC environment dependencies (separate venv)
└── .gitignore
```

> **Note:** `Retrieval-based-Voice-Conversion-WebUI/` and `YourTTS/` must be cloned separately (see Setup). They are excluded from git.

---

## ⚙️ Setup

### Prerequisites
- **Python 3.10+**
- **[ffmpeg](https://ffmpeg.org/download.html)** — must be on your `PATH`
- **Git**
- *(Optional)* NVIDIA GPU with CUDA 12.1 drivers for hardware acceleration

---

### 1. Clone the repository
```bash
git clone https://github.com/your-username/voice-clone-project.git
cd voice-clone-project
```

### 2. Create the main virtual environment
```bash
python -m venv venv

# Activate:
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

> **GPU Users:** Install PyTorch with CUDA support first:
> ```bash
> pip install torch>=2.1.0 torchaudio>=2.1.0 --index-url https://download.pytorch.org/whl/cu121
> pip install -r requirements.txt
> ```

### 3. Set up the RVC environment *(for RVC Mimic mode only)*
```bash
python -m venv rvc_env
rvc_env\Scripts\activate

pip install -r requirements-rvc.txt
```

### 4. Clone external dependencies *(for RVC Mimic mode only)*
```bash
# RVC WebUI
git clone https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI.git

# Download required RVC assets (rmvpe, hubert, etc.) per RVC documentation
# Place trained .pth model(s) in:
# Retrieval-based-Voice-Conversion-WebUI/assets/weights/
```

---

## 🏃 Running the Application

### Option A — Windows batch script (recommended)
```
scripts\start_server.bat
```

### Option B — Manual (uvicorn)
```bash
# From the project root, with venv active:
python -m uvicorn src.app:app --host 0.0.0.0 --port 8000 --workers 1
```

### Option C — Docker (GPU)
```bash
# Build and start with GPU support (requires NVIDIA Container Toolkit):
docker compose up --build

# CPU-only fallback (remove the deploy.resources block from docker-compose.yml):
docker compose up --build
```

Then open your browser at: **http://localhost:8000**

---

## 🎛️ Modes Explained

### Mode 1 — Voice Clone (TTS)
1. Upload any **reference voice** audio clip (WAV/MP3/OGG, ≥3 seconds)
2. *(Optional)* Type **custom text** to speak — otherwise the audio is transcribed
3. Choose an **accent** and **tone**, set **speed**
4. The app synthesises speech in the cloned voice using **XTTS v2**

**Supported accents:** neutral, american, british, indian, spanish, french, german, italian, portuguese, russian, japanese, korean, chinese, arabic

**Supported tones:** calm, energetic, dramatic, whisper, cheerful

---

### Mode 2 — Smart Mimic (XTTS-based)
1. Upload a **target voice** audio clip (who you want to sound like)
2. Either:
   - Type **custom text** (fast path — synthesised directly)
   - Upload a **performance audio** (transcribed first, then re-synthesised)
3. The app re-synthesises the speech using **XTTS v2** with the target voice

No RVC model required. Accent/tone from the performance audio is carried through transcription, not voice conversion.

---

### Mode 3 — RVC Mimic (Speech-to-Speech)
1. Upload a **performance audio** (the accent/tone you want to preserve)
2. Upload a **target voice** audio clip
3. RVC converts the performance audio to match the target speaker's vocal identity

> **Requirements:**
> - `Retrieval-based-Voice-Conversion-WebUI/` cloned alongside the project
> - At least one trained `.pth` model in `assets/weights/`
> - Run with `rvc_env` active

---

## 🧪 Running Tests

Run from the project root with the main `venv` active:

```bash
# Proper unit tests (no audio file needed):
python -m pytest tests/test_audio_processor.py -v

# Smoke tests (need input/recorded.wav):
python -m tests.test_tts
python -m tests.test_whisper
python -m tests.test_full_synthesis
python -m tests.test_transcription_fix

# RVC smoke test (need rvc_env + RVC repo + .pth model):
rvc_env\Scripts\activate
python -m tests.test_rvc_env

# Audio-cleaning utility (manual, set INPUT_WAV in test_voice.py):
python -m tests.test_voice
```

---

## 📦 Dependencies

### Main Environment (`requirements.txt`)

| Package | Purpose |
|---------|---------|
| `fastapi` | Web API framework |
| `uvicorn[standard]` | ASGI server |
| `python-multipart` | Form/file upload support for FastAPI |
| `TTS` (Coqui) | XTTS v2 multilingual voice synthesis |
| `faster-whisper` | Audio transcription (CTranslate2-optimised Whisper) |
| `torch` / `torchaudio` | Deep learning backend |
| `soundfile` | Audio file read/write |
| `sounddevice` | Microphone recording |
| `scipy` | Signal processing (high-pass filter) |
| `noisereduce` | Spectral-subtraction noise reduction |
| `numpy<2.0` | Numerical computing (pinned for RVC compatibility) |
| `transformers` | Required by Coqui TTS / XTTS v2 |

### RVC Environment (`requirements-rvc.txt`)

| Package | Purpose |
|---------|---------|
| `fairseq` | RVC core dependency |
| `faiss-cpu` | Feature retrieval for RVC |
| `librosa` | Audio analysis |
| `ffmpeg-python` | Audio format conversion |

---

## 🐳 Docker

The project ships with a production-ready `Dockerfile` and `docker-compose.yml`:

```bash
# Build and run (GPU — requires NVIDIA Container Toolkit + WSL2 on Windows):
docker compose up --build

# View logs:
docker compose logs -f

# Stop:
docker compose down
```

**Volumes mounted at runtime:**
- `./input` → `/app/input` — uploaded audio files
- `./output` → `/app/output` — generated audio files
- `tts-models` — XTTS v2 model cache (named volume, persists across restarts)
- `whisper-models` — Faster-Whisper model cache (named volume)

**Environment variables:**
| Variable | Default | Description |
|----------|---------|-------------|
| `WHISPER_MODEL` | `small` | Whisper model size for GPU (`base`, `small`, `medium`) |
| `WHISPER_MODEL_CPU` | `small` | Whisper model size for CPU fallback |
| `CUDA_VISIBLE_DEVICES` | `0` | GPU device index |

---

## 🗒️ Notes

- Audio files in `input/` and `output/` are **gitignored** — they will not be pushed to GitHub.
- Model weights (`.pth`, `.bin`, `.pt`, `.safetensors`) are gitignored due to file size — use [Git LFS](https://git-lfs.com/) if you need to track them.
- The RVC and YourTTS repos are external dependencies — clone them separately.
- XTTS v2 requires a speaker reference of **≥3 seconds** of clear speech for best results.
- For GPUs with ≤4GB VRAM (e.g. RTX 2050), use `WHISPER_MODEL=small` (default). The `medium` model needs ~5GB and `large-v2` needs ~10GB.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
