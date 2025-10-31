# modules/llm.py
import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL
import time

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(GEMINI_MODEL)

def gemini_response(user_text):
    if not user_text.strip():
        return "I didn't hear anything. Please speak again."
    
    try:
        prompt = f"You are a helpful voice assistant. Respond naturally and concisely.\nUser: {user_text}\nAssistant:"
        response = model.generate_content(prompt)
        reply = response.text.strip()
        print(f"Gemini: {reply}")
        return reply
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry, I couldn't process that."