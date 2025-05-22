import speech_recognition as sr    
import pyttsx3
import pyautogui
import subprocess

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def open_chrome():
    chrome_path = r"C:\Users\Public\Desktop\Google Chrome.lnk"
    try:
        subprocess.Popen(chrome_path, shell=True)
        speak("Opening Chrome")
    except Exception as e:
        print(f"Failed to open the application: {e}")
        speak("Sorry, I couldn't open the application.")

def open_linux():
    linux_path = r"C:\Users\Public\Desktop\Oracle VirtualBox.lnk"
    try:
        subprocess.Popen(linux_path, shell=True)
        speak("Opening Linux")
        # Uncomment the next line only if you need to click after opening
        pyautogui.click(x=1174, y=169)
    except Exception as e:
        print(f"Failed to open the application: {e}")
        speak("Sorry, I couldn't open the application.")

def open_cursor():
    cursor_path = r"C:\Users\lenovo\Desktop\Cursor.lnk"
    try:
        subprocess.Popen(cursor_path, shell=True)
        speak("Opening Cursor")
    except Exception as e:
        print(f"Failed to open the application: {e}")
        speak("Sorry, I couldn't open the application.")

def open_sandbox():
    sandbox_path = r"C:\Users\lenovo\Desktop\Windows Sandbox.lnk"
    try:
        subprocess.Popen(sandbox_path, shell=True)
        speak("Opening Sandbox")
    except Exception as e:
        print(f"Failed to open the application: {e}")
        speak("Sorry, I couldn't open the application.")