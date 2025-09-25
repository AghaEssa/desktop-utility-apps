 
 
 
# Phone Number Info Tool — Technical Report

## 1. Overview
A desktop app to analyze and speak details of a phone number using Python.  
It validates numbers, extracts SIM & region info, and announces results with Windows TTS.

## 2. Objectives
- Provide users quick insight about phone numbers
- Include region, carrier, timezone, and formatted output
- Add voice feedback for accessibility

## 3. Architecture
- **UI:** CustomTkinter (dark theme)
- **Phone parsing:** phonenumbers library
- **TTS:** pywin32 (SAPI.SpVoice, Zira voice)
- **Modules:** Single `main.py` script

## 4. Features
- Validate number format
- Show formatted number
- Show region, carrier, country code, timezones
- Speak results aloud
- Error handling for invalid inputs

## 5. Build Process
 
     pip install -r requirements.txt
     pyinstaller app/main.py ^
       --name "Phone_Number_Info" ^
       --onefile --windowed

## 6. Testing & Validation

Valid/invalid numbers tested

Region and carrier info displayed correctly

Voice output confirmed

Tested on Windows 10/11

## 7. Limitations

Windows-only (pywin32 TTS not cross-platform)

Requires internet for installing dependencies

Some numbers may lack carrier info

## 8. Future Work

Add offline TTS engine for cross-platform

Add bulk number lookup

Add country flag icons

Export results to file

## 9. Conclusion

Phone Number Info Tool demonstrates the use of phonenumbers + CustomTkinter + pywin32 for building a user-friendly desktop utility.
It is a practical showcase of number validation, metadata extraction, and accessibility with voice feedback.
