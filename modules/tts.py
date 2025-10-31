# modules/tts.py
from gtts import gTTS
import pygame
import time
import os
from config import TEMP_DIR

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

def text_to_speech(text):
    if not text:
        return None
    mp3_file = os.path.join(TEMP_DIR, f"out_{int(time.time()*1000)}.mp3")
    try:
        tts = gTTS(text, lang='en')
        tts.save(mp3_file)
        return mp3_file
    except Exception as e:
        print(f"TTS Failed: {e}")
        return None

def play_audio(file_path):
    if not file_path or not os.path.exists(file_path):
        return
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print("Speaking...")
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except Exception as e:
        print(f"Playback Error: {e}")