# modules/stt.py
import os
import whisper
from config import MODEL_NAME

print("Loading Whisper model... (one-time)")
model = whisper.load_model(MODEL_NAME)
print(f"Whisper '{MODEL_NAME}' loaded.")

def speech_to_text(audio_file):
    if not audio_file or not os.path.exists(audio_file):
        return ""
    try:
        result = model.transcribe(audio_file, language="en", fp16=False)
        text = result["text"].strip()
        print(f"STT: '{text}'")
        return text
    except Exception as e:
        print(f"STT Error: {e}")
        return ""