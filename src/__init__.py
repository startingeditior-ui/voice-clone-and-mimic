"""
Voice Clone Project — src package.

Modules:
    app             FastAPI application (main entry point)
    transcribe      Faster-Whisper audio transcription
    synthesize      XTTS v2 voice synthesis (TTS Clone + Smart Mimic)
    audio_processor Pre- and post-processing utilities for voice cloning
    rvc_wrapper     Retrieval-based Voice Conversion (RVC) wrapper
    record_audio    Microphone recording utility
    main_pipeline   CLI pipeline: record → transcribe → synthesize
"""
