# Voice Agent

A simple voice agent using local Whisper for STT and gTTS for TTS.

## Setup
1. Activate virtual env: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows).
2. Install deps: `pip install -r requirements.txt`
3. Run: `python main.py`

## Usage
- Speak when prompted.
- Say "exit" to quit.
- Temp audio files are saved in `temp_audio/`.

## Customization
- Change `MODEL_NAME` in `main.py` for better accuracy (e.g., "small").
- Extend `generate_response()` for AI integration (e.g., call an LLM API).