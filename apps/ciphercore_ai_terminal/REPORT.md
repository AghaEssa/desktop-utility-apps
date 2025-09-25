# CipherCore AI Terminal — Technical Report

## 1. Overview
CipherCore AI Terminal is a desktop chatbot that integrates Google Gemini AI into a custom terminal-style interface.  
The app enhances user interaction with typing animations and sound effects, while ensuring API keys are securely managed.

## 2. Objectives
- Build a desktop AI app with simple installation (EXE)
- Provide responsive and interactive UI
- Demonstrate secure handling of API keys
- Enable reproducible builds with PyInstaller

## 3. Architecture
- **UI:** CustomTkinter (dark theme, textbox + entry)
- **Audio:** Pygame mixer for sound events
- **LLM:** Google Generative AI SDK (gemini-1.5-flash)
- **Secrets:** `.env` file via python-dotenv
- **Packaging:** PyInstaller onefile EXE

## 4. Workflow
1. User enters prompt
2. Sound effect plays (`type.wav`)
3. Gemini API processes the input
4. Response displayed with typing animation
5. Startup/shutdown sounds on app open/close

## 5. Security
- No API key in code or repo
- `.env` file is git-ignored
- `.env.example` provided for reference

 
## 6. Build Process
 
     pip install -r requirements.txt
     pyinstaller app/main.py ^
       --name "CipherCore_AI_Terminal" ^
       --onefile --windowed ^
       --add-data "app/sounds;sounds"





## 7. Testing & Validation

Verified sounds trigger correctly

Prompt → AI response works with animation

Exit command shuts app with sound

EXE tested on Windows 10/11

## 8. Limitations

Windows-only EXE (cross-platform build requires extra work)

SmartScreen warning (unsigned EXE)

Requires stable internet

## 9. Future Work

Add conversation history

Support streaming tokens

Add model selector & temperature

Integrate TTS / voice input

## 10. Conclusion

CipherCore AI Terminal demonstrates how to package a modern AI-driven desktop app using Python.
The design balances usability, aesthetics, and security, making it a solid base for further extensions.