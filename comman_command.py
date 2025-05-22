import tkinter as tk
import os

from google import genai
from google.genai import types
import google.generativeai as genai
import speech_recognition as sr    
import webbrowser
import pyttsx3
import pyautogui
import pyperclip
import subprocess
import datetime
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()


# Speak function
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


def tell_time():
    """Tell the current time."""
    hour = datetime.datetime.now().strftime("%I")
    minute = datetime.datetime.now().strftime("%M")
    am_pm = datetime.datetime.now().strftime("%p")
    print(f"Sir, the time is {hour} {minute} {am_pm}") 
    speak(f"Sir, the time is {hour} {minute} {am_pm}") 

def close_app_window():
    pyautogui.click(x=1881, y=15)  # Adjust coordinates for your screen resolution
    time.sleep(3)
    speak("Exiting the site")
    
def play_music():
    """Play music on YouTube."""
    speak("Please tell me the name of the song.")
    song_name = voice_input()
    if song_name:
        speak(f"Playing {song_name} on YouTube.")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")
        time.sleep(5)
        pyautogui.click(x=662, y=319)  # Adjust coordinates for your screen resolution
    