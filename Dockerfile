# ──────────────────────────────────────────────────────────────────────────────
# Voice Clone Project — Dockerfile
# Base: NVIDIA CUDA 12.1 + cuDNN 8 on Ubuntu 22.04
# Exposes FastAPI on port 8000
# ──────────────────────────────────────────────────────────────────────────────

FROM nvidia/cuda:12.1.0-cudnn8-runtime-ubuntu22.04

# ── Labels ────────────────────────────────────────────────────────────────────
LABEL maintainer="voice-clone-project"
LABEL description="Voice Cloning App — FastAPI + XTTS + Faster-Whisper"

# ── System dependencies ────────────────────────────────────────────────────────
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.10 \
    python3.10-dev \
    python3-pip \
    ffmpeg \
    libsndfile1 \
    libsndfile1-dev \
    libportaudio2 \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Make python3.10 the default python
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1 \
 && update-alternatives --install /usr/bin/pip    pip    /usr/bin/pip3     1

# ── Working directory ──────────────────────────────────────────────────────────
WORKDIR /app

# ── Python dependencies ────────────────────────────────────────────────────────
# Copy requirements first (layer-cache friendly)
COPY requirements.txt .

# Install PyTorch with CUDA 12.1 support explicitly, then everything else
RUN pip install --upgrade pip && \
    pip install torch>=2.1.0 torchaudio>=2.1.0 --index-url https://download.pytorch.org/whl/cu121 && \
    pip install --no-cache-dir -r requirements.txt

# ── Application source ─────────────────────────────────────────────────────────
COPY src/       ./src/
COPY frontend/  ./frontend/

# Create input/output dirs (mounted as volumes at runtime)
RUN mkdir -p /app/input /app/output

# ── Model cache directories (mounted as named volumes) ─────────────────────────
# XTTS models
ENV COQUI_HOME=/root/.local/share/tts
# Faster-Whisper / CTranslate2 models
ENV HF_HOME=/root/.cache/huggingface

RUN mkdir -p $COQUI_HOME $HF_HOME

# ── Port ───────────────────────────────────────────────────────────────────────
EXPOSE 8000

# ── Healthcheck ────────────────────────────────────────────────────────────────
HEALTHCHECK --interval=30s --timeout=10s --start-period=120s --retries=3 \
    CMD curl -f http://localhost:8000/ || exit 1

# ── Entrypoint ─────────────────────────────────────────────────────────────────
CMD ["python", "-m", "uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
