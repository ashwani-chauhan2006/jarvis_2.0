# AI Assistant GUI

This project is a desktop AI assistant with a graphical user interface (GUI) built using Python and Tkinter. It supports chat, voice input, news headlines, app launching, music, time queries, and more. The assistant uses Google Gemini for AI chat and integrates with various APIs and local utilities.

---

## Features

- **Chat with AI:** Type or speak your queries and get AI-powered responses.
- **Voice Input:** Click the mic button to speak your message (uses Google Speech Recognition).
- **News Headlines:** Type "news" to get the latest technology news headlines.
- **Open Websites/Apps:** Commands like "open youtube", "open chrome", "open linux", etc.
- **Play Music:** Type "music" to play music.
- **Tell Time:** Type "time" to get the current time.
- **Send WhatsApp Messages:** Type "message" to open WhatsApp messaging.
- **Shutdown:** Type "jarvis shutdown" to close the assistant.
- **Responsive GUI:** Chat box, input, and buttons resize with the window.
- **Background Images:** Right side displays background images for visual appeal.

---

## Requirements

- Python 3.7+
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (usually included with Python)
- [requests](https://pypi.org/project/requests/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [google-generativeai](https://pypi.org/project/google-generativeai/)
- [pyaudio](https://pypi.org/project/PyAudio/) (for microphone input)
- Other project files: `open_sites.py`, `open_app.py`, `ai_pro.py`, `message_what.py`, `comman_command.py`
- A valid [NewsAPI](https://newsapi.org/) API key

---

## Setup

1. **Clone the repository** and place all required `.py` files in the same directory.
2. **Install dependencies:**
    ```bash
    pip install requests pyttsx3 SpeechRecognition google-generativeai pyaudio
    ```
3. **Download or provide a `back.png` image** in the same directory as `gui.py` for background visuals.
4. **Set your NewsAPI key** in the `get_news` function in `gui.py`:
    ```python
    api_key = 'YOUR_NEWSAPI_KEY'
    ```
5. **Run the assistant:**
    ```bash
    python gui.py
    ```

---

## Usage

- **Type** your message and press Enter or click "Send".
- **Click the mic button** to speak your message.
- **Try commands** like:
    - `news`
    - `open youtube`
    - `open chrome`
    - `music`
    - `time`
    - `message`
    - `jarvis shutdown`

---

## File Structure

- `gui.py` — Main GUI and logic
- `open_sites.py` — Functions to open websites
- `open_app.py` — Functions to open desktop apps
- `ai_pro.py` — AI chat logic
- `message_what.py` — WhatsApp messaging logic
- `comman_command.py` — Common commands (time, music, etc.)
- `back.png` — Background image

---

## Notes

- Make sure your microphone is connected for voice input.
- Some features (like WhatsApp messaging) may require additional setup or permissions.
- The NewsAPI free tier may have request limits.

---

## License

This project is for educational and personal use.

---