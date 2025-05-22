import webbrowser

def open_sites(query, speak=print):
    sites = [
        ["youtube", "https://www.youtube.com"],
        ["wikipedia", "https://www.wikipedia.com"],
        ["google", "https://www.google.com"],
        ["instagram", "https://www.instagram.com"],
        ["whatsapp", "https://www.whatsapp.com"],
        ["github", "https://www.github.com"]
    ]
    for site in sites:
        if f"open {site[0]}" in query:
            speak(f"Opening {site[0]} sir...")
            webbrowser.open(site[1])
            return True
    return False