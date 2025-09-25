import customtkinter as ctk
import google.generativeai as genai
import pygame
import os
import time
import sys




# ==== Sound Setup ====
pygame.init()
pygame.mixer.init()



# ✅ Dynamic path handler (works in .py and .exe both)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # for PyInstaller .exe
    except Exception:
        base_path = os.path.abspath(".")  # for running directly
    return os.path.join(base_path, relative_path)



# ✅ Updated sound loader
def play_sound(file):
    try:
        sound_path = resource_path(os.path.join("sounds", file))
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
    except Exception as e:
        print("Sound error:", e)



# ==== Gemini Config ====
genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel("gemini-1.5-flash")


# ==== UI Setup ====
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("👾 CipherCore AI Terminal v1.0 — by Agha Essa")
app.geometry("650x560")
app.resizable(False, False)
app.configure(bg="#0f0f0f")



# ==== Play startup sound ====
play_sound("startup.wav")


# ==== Fonts ====
font_main = ctk.CTkFont(family="Consolas", size=16, weight="bold")
font_title = ctk.CTkFont(family="Consolas", size=25, weight="bold")

# ==== Title ====
title_label = ctk.CTkLabel(
    app,
    text="👾 CipherCore AI Terminal",
    font=font_title,
    text_color="#00ffff"
)
title_label.pack(pady=10)

# ==== Output Frame ====
output_frame = ctk.CTkFrame(app, fg_color="#1a1a1a", corner_radius=10)
output_frame.pack(pady=10)

output_text = ctk.CTkTextbox(
    output_frame,
    width=600,
    height=300,
    font=font_main,
    wrap="word",
    fg_color="#1a1a1a",
    text_color="#00ffcc",
    corner_radius=0
)
output_text.pack(padx=10, pady=10)

# ==== Input Field ====
input_frame = ctk.CTkFrame(app, fg_color="#1a1a1a", corner_radius=10)
input_frame.pack(pady=10)

input_entry = ctk.CTkEntry(
    input_frame,
    placeholder_text="Type your prompt...",
    width=500,
    font=font_main,
    fg_color="#141414",
    border_color="#00ffcc",
    border_width=2,
    text_color="#ff0000"
)
input_entry.pack(pady=10, padx=10)




# ==== Typing Animation ====
def type_response(response_text):
    play_sound("gemini_beep.wav")
    output_text.insert("end", "💬 CipherCore: ")
    output_text.update()
    for char in response_text:
        output_text.insert("end", char)
        output_text.update()
        time.sleep(0.015)  # smooth typing delay
    output_text.insert("end", "\n\n")
    output_text.see("end")


# ==== Chat Function ====
def chat():
    prompt = input_entry.get().strip()
    if prompt.lower() == "exit":
        play_sound("shutdown.wav")
        app.after(1000, app.quit)
    elif prompt:
        play_sound("type.wav")
        output_text.insert("end", f"\n🧠 You: {prompt}\n", "user")
        output_text.insert("end", "🤖 CipherCore is thinking...\n")
        app.update()
        try:
            response = model.generate_content(prompt)
            output_text.delete("end-2l", "end-1l")  # remove thinking...
            type_response(response.text.strip())
        except Exception as e:
            output_text.insert("end", f"⚠️ Error: {str(e)}\n")
        input_entry.delete(0, "end")

# ==== Bind Enter ====
input_entry.bind("<Return>", lambda event: chat())

# ==== Send Button ====
send_btn = ctk.CTkButton(
    app,
    text="💬 Send",
    command=chat,
    fg_color="#E5A00C",
    hover_color="#00b3b3",
    font=font_main
)
send_btn.pack(pady=10)

# ==== Exit Sound on Close ====
def on_close():
    play_sound("shutdown.wav")
    app.after(1000, app.destroy)

app.protocol("WM_DELETE_WINDOW", on_close)

# ==== Run App ====
app.mainloop()
