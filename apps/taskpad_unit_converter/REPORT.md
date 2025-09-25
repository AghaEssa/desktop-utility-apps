# TaskPad Unit Converter — Technical Report

## 1. Overview
TaskPad Unit Converter is a compact desktop utility that merges a **Unit Converter** with a **To-Do List** inside a single CustomTkinter window.  
It is designed for quick daily usage with minimal dependencies and a clean dark UI.

## 2. Objectives
- Provide a single-window desktop utility for common conversions
- Combine productivity (to-do list) with utility (unit converter)
- Keep the app lightweight, easy to run, and portable (EXE packaging)

## 3. Architecture
- **UI Framework:** CustomTkinter (dark theme)
- **Core Script:** `main.py`
- **Widgets Used:**
  - ComboBoxes for selecting unit types
  - Entry fields for input/output
  - Buttons for converting, adding, deleting tasks
  - Textbox for managing tasks

## 4. Features
- Length Conversion: Km ⇄ Miles  
- Weight Conversion: Kg ⇄ Pounds  
- Temperature Conversion: °C ⇄ °F  
- To-Do List:
  - Add new task
  - Click to highlight task
  - Delete selected task
  - Clear all tasks
- Input validation and basic error messaging

## 5. Build Process
 
    pip install -r requirements.txt
    pyinstaller app/main.py ^
      --name "TaskPad_Unit_Converter" ^
      --onefile --windowed



## 6. Testing & Validation

Verified accuracy of conversions with sample values

Task add, select, delete, and clear flows tested

UI responsiveness confirmed

Build tested on Windows 10/11

## 7. Limitations / Future Work

Current tasks do not persist (cleared on app close)

Limited unit categories (only Length, Weight, Temperature)

Build tested primarily for Windows

Future improvements:

Add persistence (save tasks to file/DB)

Add more unit types (area, volume, speed)

Add hotkeys or system tray support

Cross-platform packaging

## 8. Conclusion

TaskPad Unit Converter successfully demonstrates how a simple productivity tool can be built with Python and CustomTkinter.
It balances usability and simplicity, making it a practical example of combining utilities in one app while being easy to package as a standalone EXE.






