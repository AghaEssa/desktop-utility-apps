# 👾 CipherCore AI Terminal

A polished desktop AI terminal built with **Python (CustomTkinter + Pygame)** and packaged with **PyInstaller**.  
Features typing animation, system sounds, and secure `.env`-based API key handling.

## ✨ Features
- Dark themed UI with terminal look
- Typing animation for AI responses
- Startup, typing, and shutdown sounds
- Secure API key loading from `.env`
- Packaged into a single Windows EXE

## 📂 Project Structure
ciphercore_ai_terminal/\
│── app/\
│ ├── main.py\
│ └── sounds/ (startup.wav, shutdown.wav, gemini_beep.wav,\ type.wav)\
│── .env.example\
│── requirements.txt\
│── REPORT.md\
│── README.md\


## 🚀 Usage
1. Create virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # on Windows


 
2 . Install dependencies:

     pip install -r requirements.txt


3  Create .env from example and add your key:

    GEMINI_API_KEY=your_api_key_here


4   Run:

    python app/main.py

 


📜 License

MIT


