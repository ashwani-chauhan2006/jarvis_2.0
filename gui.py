import tkinter as tk
import os
from google import genai
import google.generativeai as genai
import speech_recognition as sr    
import pyttsx3

from open_sites import open_sites
from open_app import open_chrome, open_linux, open_cursor, open_sandbox
from ai_pro import gen_ai
from message_what import message_what
from comman_command import tell_time, close_app_window, play_music


# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

model = genai.GenerativeModel("gemini-2.0-flash-exp")
chat = model.start_chat()

# Speak function
def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

listening = False  # Flag to control continuous listening

def voice_input():
    global listening
    listening = True
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        chat_box.config(state="normal")
        chat_box.insert(tk.END, "Listening for 5 seconds...\n", "ai")
        chat_box.config(state="disabled")
        root.update()
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            text = recognizer.recognize_google(audio, language="en-in")
            user_input.delete(0, tk.END)
            user_input.insert(0, text)
            send_message()  # Automatically send after recognition
        except sr.UnknownValueError:
            chat_box.config(state="normal")
            chat_box.insert(tk.END, "AI: Sorry, could not understand your voice.\n", "ai")
            chat_box.config(state="disabled")
        except Exception as e:
            chat_box.config(state="normal")
            chat_box.insert(tk.END, f"AI: Error: {str(e)}\n", "ai")
            chat_box.config(state="disabled")
    # Continue listening only if flag is True
    if listening:
        root.after(500, voice_input)


def stop_listening(event=None):
    global listening
    listening = False
    user_input.focus_set()  # Focus the input box for typing

def send_message():
    user_msg = user_input.get()
    if user_msg.strip():
        chat_box.config(state="normal")
        # First insert user message
        chat_box.insert(tk.END, f"You: {user_msg}\n", "user")
        msg_lower = user_msg.lower()

        # Check for shutdown first
        if "jarvis shutdown" in msg_lower:
            chat_box.insert(tk.END, "AI: Goodbye, sir. Have a great day!\n", "ai")
            chat_box.see(tk.END)
            chat_box.config(state="disabled")
            speak("Goodbye, sir. Have a great day!")
            root.destroy()
            return

        elif "close" in msg_lower:
            chat_box.insert(tk.END, "AI: Closing the application...\n", "ai")
            chat_box.see(tk.END)
            chat_box.config(state="disabled")
            close_app_window()

        elif "time" in msg_lower:
            time_response = tell_time()
            chat_box.insert(tk.END, f"AI: {time_response}\n", "ai")
            chat_box.see(tk.END)
            chat_box.config(state="disabled")
            speak(time_response)

        elif "music" in msg_lower:
            chat_box.insert(tk.END, "AI: Playing music...\n", "ai")
            chat_box.see(tk.END)
            chat_box.config(state="disabled")
            play_music()

        elif "message" in msg_lower:
            chat_box.insert(tk.END, "AI: Opening messaging...\n", "ai")
            chat_box.see(tk.END)
            chat_box.config(state="disabled")
            message_what()
        
        elif "chrome" in msg_lower:
            chat_box.insert(tk.END, "AI: Opening Chrome...\n", "ai")
            chat_box.see(tk.END)
            chat_box.config(state="disabled")
            open_chrome()
                
        elif "linux" in msg_lower:
            chat_box.insert(tk.END, "AI: Opening Linux...\n", "ai")
            chat_box.see(tk.END)
            chat_box.config(state="disabled")
            open_linux()
        
        elif "cursor" in msg_lower:
            chat_box.insert(tk.END, "AI: Opening Cursor...\n", "ai")
            chat_box.see(tk.END)
            chat_box.config(state="disabled")
            open_cursor()
        
        elif "sandbox" in msg_lower:
            chat_box.insert(tk.END, "AI: Opening Sandbox...\n", "ai")
            chat_box.see(tk.END)
            chat_box.config(state="disabled")
            open_sandbox()
        
        elif "open " in msg_lower:
            chat_box.insert(tk.END, "AI: Opening the site...\n", "ai")
            chat_box.see(tk.END)
            chat_box.config(state="disabled")
            speak("opening the site")
            open_sites(msg_lower)
        else:
            try:
                response = chat.send_message(user_msg)
                chat_box.insert(tk.END, f"AI: {response.text}\n", "ai")
                chat_box.see(tk.END)
                chat_box.config(state="disabled")
                speak(response.text)
            except Exception as e:
                error_msg = f"AI: Sorry, there was an error: {e}\n"
                chat_box.insert(tk.END, error_msg, "ai")
                chat_box.see(tk.END)
                chat_box.config(state="disabled")
                speak(f"Sorry, there was an error: {e}")
            
    else:
        chat_box.insert(tk.END, "AI: Please enter a message.\n", "ai")
        chat_box.see(tk.END)
        chat_box.config(state="disabled")

    user_input.delete(0, tk.END)

root = tk.Tk()
root.title("AI Assistant")
root.geometry("1200x1000")
root.configure(bg="black")

# Create main container frame
main_container = tk.Frame(root, bg="black")
main_container.pack(fill=tk.BOTH, expand=True)

# Left section (half of the window) - Chat interface
left_section = tk.Frame(main_container, bg="black", width=600)
left_section.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Title
title = tk.Label(left_section, text="AI Assistant", font=("Segoe UI", 24, "bold"), bg="black", fg="#0e2047")
title.pack(pady=20)

# Chat box
chat_box = tk.Text(
    left_section,
    font=("Segoe UI", 12),
    bg="black",
    fg="#fffffe",
    height=25,
    width=50,
    state="disabled",
    wrap="word",
    bd=0,
    highlightthickness=0
)
chat_box.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 10))

chat_box.tag_config("user", foreground="#eebbc3")
chat_box.tag_config("ai", foreground="#a1a1aa")

# Bottom frame for input elements
bottom_frame = tk.Frame(left_section, bg="black")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)

# User input frame
input_frame = tk.Frame(bottom_frame, bg="black")
input_frame.pack(fill=tk.X)

user_input = tk.Entry(
    input_frame,
    font=("Segoe UI", 11),
    width=30,
    bg="#1a1a2e",
    fg="white",
    bd=1,
    relief="solid",
    highlightthickness=1,
    highlightbackground="#0e2047",
    insertbackground="white"
)
user_input.pack(side=tk.LEFT, padx=(0,5), ipady=4, fill=tk.X, expand=True)
user_input.bind("<Return>", lambda event: send_message())
user_input.bind("<Button-1>", stop_listening)

send_btn = tk.Button(
    input_frame,
    text="Send",
    font=("Segoe UI", 11, "bold"),
    bg="#0e2047",
    fg="white",
    bd=0,
    padx=15,
    pady=4,
    command=send_message,
    activebackground="#1a1a2e",
    activeforeground="white"
)
send_btn.pack(side=tk.LEFT, padx=2)

mic_btn = tk.Button(
    input_frame,
    text="🎤",
    font=("Segoe UI", 11),
    bg="#0e2047",
    fg="white",
    bd=0,
    padx=8,
    pady=4,
    command=voice_input,
    activebackground="#1a1a2e",
    activeforeground="white"
)
mic_btn.pack(side=tk.LEFT)

# Right section (two quarters) - Background images
right_section = tk.Frame(main_container, bg="black", width=600)
right_section.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Load and display background image in both quarters
script_dir = os.path.dirname(os.path.abspath(__file__))
bg_path = os.path.join(script_dir, "back.png")
bg_img = tk.PhotoImage(file=bg_path)

# Top quarter
top_quarter = tk.Frame(right_section, bg="black")
top_quarter.pack(fill=tk.BOTH, expand=True)
bg_label1 = tk.Label(top_quarter, image=bg_img, bg="black")
bg_label1.pack(fill=tk.BOTH, expand=True)

# Bottom quarter
bottom_quarter = tk.Frame(right_section, bg="black")
bottom_quarter.pack(fill=tk.BOTH, expand=True)
bg_label2 = tk.Label(bottom_quarter, image=bg_img, bg="black")
bg_label2.pack(fill=tk.BOTH, expand=True)

# Start voice input automatically after a short delay
def start_voice_input():
    chat_box.config(state="normal")
    chat_box.insert(tk.END, "AI: Voice input is active. You can start speaking...\n", "ai")
    chat_box.see(tk.END)
    chat_box.config(state="disabled")
    voice_input()

# Schedule the voice input to start after 1 second
root.after(1000, start_voice_input)

root.mainloop()