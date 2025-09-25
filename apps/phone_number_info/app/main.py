import customtkinter as ctk
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import win32com.client



# Initialize TTS engine (Zira voice, if available)
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Rate = 2
for voice in speaker.GetVoices():
    if "zira" in voice.GetDescription().lower():
        speaker.Voice = voice
        break




# App logic
def track_number():
    phone = phone_entry.get().strip()
    if not phone:
        ctk.CTkMessagebox(title="Input Error", message="Please enter a phone number.", icon="warning")
        return

    try:
        number_obj = phonenumbers.parse(phone, None)
        if not phonenumbers.is_valid_number(number_obj):
            result_text.set("❌ Invalid phone number.")
            speaker.speak("This phone number is not valid.")
            return

        region = geocoder.description_for_number(number_obj, "en")
        sim = carrier.name_for_number(number_obj, "en")
        zones = timezone.time_zones_for_number(number_obj)
        formatted = phonenumbers.format_number(number_obj, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

        output = (
            f"📱 Formatted: {formatted}\n"
            f"🌍 Region: {region}\n"
            f"📡 Carrier: {sim}\n"
            f"🌐 Country Code: {number_obj.country_code}\n"
            f"⏰ Timezone(s): {', '.join(zones)}"
        )

        result_text.set(output)
        speaker.speak(f"This number is from {region}. Time zone is {', '.join(zones)}.")

    except Exception as e:
        result_text.set("⚠️ Error: Invalid format or unknown number.")
        speaker.speak("Something went wrong. Only valid numbers are accepted.")

# UI Setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("📍 SIM & Region Locator v1.0 – by Agha Essa")
app.geometry("520x400")
app.resizable(False, False)

# Widgets
title = ctk.CTkLabel(app, text="SIM & Region Locator", font=("Segoe UI", 20, "bold"), text_color="cyan")
title.pack(pady=15)

phone_entry = ctk.CTkEntry(app, width=300, placeholder_text="Enter phone number (e.g., +92...)")
phone_entry.insert(0, "+92")
phone_entry.pack(pady=10)

track_btn = ctk.CTkButton(app, text="🔍 Track Number", command=track_number)
track_btn.pack(pady=10)

result_text = ctk.StringVar()
result_label = ctk.CTkLabel(app, textvariable=result_text, font=("Segoe UI", 14), justify="left", wraplength=500, text_color="#00ff88")
result_label.pack(pady=20)

exit_btn = ctk.CTkButton(app, text="❌ Exit", command=app.destroy, fg_color="#cc0000", hover_color="#a30000")
exit_btn.pack(pady=5)

app.mainloop()
