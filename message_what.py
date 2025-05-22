import speech_recognition as sr  
import pyttsx3
import pyautogui
import webbrowser
import time
import pyperclip

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def voice_input():
    """Capture voice input and return as text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=5)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            speak("Sorry, I did not understand.")
            return None
        except Exception as e:
            speak(f"Error: {e}")
            return None

def message_what():
    """Send a message on WhatsApp."""
    speak("Please tell me the message.")
    message = voice_input()
    if message:
        speak("Please tell me the name of the contact.")
        contact = voice_input()
        if contact:
            speak(f"Sending message to {contact}.")
            webbrowser.open("https://web.whatsapp.com/")
            time.sleep(10)  # Wait for WhatsApp Web to load
            pyperclip.copy(message)
            pyautogui.click(x=239, y=313)  # Adjust coordinates for the search bar
            time.sleep(3)
            pyautogui.write(contact)
            time.sleep(5)
            pyautogui.press("enter")
            time.sleep(2)
            pyautogui.click(x=1086, y=965)  # Adjust coordinates for the message box
            pyautogui.hotkey("ctrl", "v")
            time.sleep(2)
            pyautogui.press("enter")
            speak("Message sent successfully.")