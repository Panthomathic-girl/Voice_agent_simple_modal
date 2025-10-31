# main.py
import time
import os
from modules.audio import select_mic, record_audio
from modules.stt import speech_to_text
from modules.llm import gemini_response
from modules.tts import text_to_speech, play_audio
from config import LOG_DIR
import pygame

# Select mic once
MIC_DEVICE = select_mic()
if MIC_DEVICE is not None:
    import sounddevice as sd
    sd.default.device[0] = MIC_DEVICE

# Log file
LOG_FILE = os.path.join(LOG_DIR, "conversation.log")

def log_conversation(user, agent):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"User: {user}\nAgent: {agent}\n\n")

def main():
    print("\n" + "="*70)
    print("   VOICE AGENT WITH GEMINI AI IS READY!")
    print("   Speak into your Bluetooth earpods. Say 'bye' to exit.")
    print("="*70)

    try:
        while True:
            # 1. Record
            audio_file = record_audio(MIC_DEVICE)
            if not audio_file:
                continue

            # 2. STT
            user_text = speech_to_text(audio_file)
            if not user_text:
                user_text = "[no speech]"

            # 3. LLM
            if "bye" in user_text.lower() or "exit" in user_text.lower():
                reply = "Goodbye! Have a great day."
            else:
                reply = gemini_response(user_text)

            # 4. TTS + Play
            mp3_file = text_to_speech(reply)
            print(f"Agent: {reply}")
            if mp3_file:
                play_audio(mp3_file)

            # 5. Log
            log_conversation(user_text, reply)

            # 6. Exit
            if "bye" in user_text.lower() or "exit" in user_text.lower():
                break

            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        pygame.mixer.quit()

if __name__ == "__main__":
    main()