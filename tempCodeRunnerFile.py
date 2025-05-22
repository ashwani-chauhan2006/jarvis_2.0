

root = tk.Tk()
root.title("AI Assistant")
root.geometry("500x600")
root.configure(bg="black")

# --- Background image ---
script_dir = os.path.dirname(os.path.abspath(__file__))
bg_path = os.path.join(script_dir, "back.png")
bg_img = tk.PhotoImage(file=bg_path)
bg_label = tk.Label(root, image=bg_img, bg="black")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Title
title = tk.Label(root, text="AI Assistant", font=("Segoe UI", 20, "bold"), bg="black", fg="#eebbc3")
title.pack(pady=20)

# Chat box
chat_box = tk.Text(
    root,
    font=("Segoe UI", 12),
    bg="black",
    fg="#fffffe",
    height=20,
    width=70,
    state="disabled",
    wrap="word",
    bd=0,
    highlightthickness=0
)
chat_box.tag_config("user", foreground="#eebbc3")
chat_box.tag_config("ai", foreground="#a1a1aa")
chat_box.pack(padx=10, pady=10)

# User input frame
input_frame = tk.Frame(root, bg="black")
input_frame.pack(pady=10)

user_input = tk.Entry(input_frame, font=("Segoe UI", 12), width=32, bg="black", fg="#fffffe", bd=1, relief="solid", highlightthickness=0, insertbackground="#eebbc3")
user_input.pack(side=tk.LEFT, padx=(0,10), ipady=6)
user_input.bind("<Return>", lambda event: send_message())
user_input.bind("<Button-1>", stop_listening)  # Stop voice input and focus when clicked

send_btn = tk.Button(
    input_frame,
    text="Send",
    font=("Segoe UI", 12, "bold"),
    bg="#eebbc3",
    fg="black",
    bd=0,
    padx=20,
    pady=6,
    command=send_message,
    activebackground="#eebbc3",
    activeforeground="black"
)
send_btn.pack(side=tk.LEFT)

mic_btn = tk.Button(
    input_frame,
    text="🎤",
    font=("Segoe UI", 12),
    bg="#22223b",
    fg="#eebbc3",
    bd=0,
    padx=10,
    pady=6,
    command=voice_input,
    activebackground="#eebbc3",
    activeforeground="black"
)
mic_btn.pack(side=tk.LEFT)

root.mainloop()