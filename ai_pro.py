from google import genai
import google.generativeai as genai
import speech_recognition as sr    
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


API_KEY = "AIzaSyD_E8mcnGagr9GFxWvpPLuf8K6YknCQvvE"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash-exp")
chat = model.start_chat()

# Speak function
def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()


def gen_ai():
    while True:
        query = input("you: ")
        if query.lower() == "exit":
            break
        try:
            response = chat.send_message(query)
            speak(f"{response.text}")
            speak(f"gemini: {response.text}")
        except Exception as e:
            print("Error:", e)
