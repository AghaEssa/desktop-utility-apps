 # 📍 SIM & Region Locator

A desktop utility built with **Python (CustomTkinter, phonenumbers, pywin32)** that detects details of a phone number including **region, carrier, country code, and timezone**.  
Also speaks the result aloud using Windows TTS (Zira voice if available).

## ✨ Features
- Input a phone number (E.164 format, e.g. `+92...`)
- Validate and format numbers
- Detect region, carrier, country code, and timezones
- Text-to-speech output using Windows SAPI (Zira)
- Modern dark UI (CustomTkinter)

## 📂 Project Structure
phone_number_info/\
│── app/\
│ └── main.py\
│── requirements.txt\
│── README.md\
│── REPORT.md\



## 🚀 Run (from source)


     pip install -r requirements.txt
     python app/main.py
     
##  📦 Build Executable
     pyinstaller app/main.py ^
       --name "Phone_Number_Info" ^
       --onefile --windowed
⚠️ Note: pywin32 TTS works on Windows only.

##   📜 License

MIT