# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# === API KEYS ===
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or "your-gemini-api-key-here"

# === AUDIO SETTINGS ===
SAMPLE_RATE = 16000
RECORD_SECONDS = 5
MODEL_NAME = "base"  # tiny / base / small

# === PATHS ===
TEMP_DIR = "temp_audio"
LOG_DIR = "logs"
os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# === GEMINI MODEL ===
GEMINI_MODEL = "gemini-2.5-flash"  # Fast & cheap