# 🖥️ Desktop Utility Apps

[![Download latest](https://img.shields.io/github/v/release/AghaEssa/desktop-utility-apps?label=download%20latest%20release)](https://github.com/AghaEssa/desktop-utility-apps/releases/latest)


A collection of lightweight desktop applications built with **Python** and packaged into standalone executables with **PyInstaller**.  
Each app is designed to be user-friendly, portable, and easy to install on Windows.

---

## 📦 Included Apps

| App Name                  | Description                                                                 | Status  |
|---------------------------|-----------------------------------------------------------------------------|---------|
| **CipherCore AI Terminal**| AI chatbot with typing animation, sounds, and secure `.env` API key handling | ✔️ Added |
| **Blogsite_CT**           | Multi-page desktop blogsite (Login/Signup, Blog, Gallery, About)            | ✔️ Added |
| **TaskPad Unit Converter**| Unit Converter (Km/Miles, Kg/Pounds, °C/°F) + To-Do List                    | ✔️ Added |
| **Phone Number Info Tool**| Detects phone number region, carrier, timezone + TTS voice output           | ✔️ Added |

---
 

## 📂 Repository Structure
desktop-utility-apps/\
│── apps/\
│   ├── ciphercore_ai_terminal/     #    AI chatbot app\
│   ├── blogsite_ct/              # Blogsite desktop app\
│   ├── taskpad_unit_converter/   # Unit Converter + To-Do List\
│   └── phone_number_info/        # Phone number info tool\
│── README.md\
│── .gitignore\


 

## 🛠️ Tech Stack
- Python
- CustomTkinter
- Pillow (image handling for Blogsite_CT)
- Pygame (sound handling for CipherCore AI Terminal)
- python-dotenv (secure API key management for CipherCore)
- phonenumbers + pywin32 (for Phone Number Info Tool)
- PyInstaller (packaging)

 

## 🚀 Getting Started
Each app has its own folder under `/apps/` with:
- `app/` → source code
- `requirements.txt` → dependencies
- `README.md` → usage instructions
- `REPORT.md` → technical documentation
 

 
## 📦 Building Executables
Each app can be packaged into a standalone EXE with **PyInstaller**.

Example (CipherCore AI Terminal):
 
     pyinstaller app/main.py ^
    --name "CipherCore_AI_Terminal" ^
    --onefile --windowed ^
    --add-data "app/sounds;sounds"

The executable will be created in the dist/ folder.



## 📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute these apps with proper attribution.


## 👤 Author

Agha Essa Khan
Passionate about building secure, user-friendly, and portable desktop tools.
