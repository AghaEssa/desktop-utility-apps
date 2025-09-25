# ✅ TaskPad Unit Converter

A minimal **desktop utility** built with **CustomTkinter** that combines a **Unit Converter** (Length, Weight, Temperature) with a lightweight **To-Do List**.

## ✨ Features
- Length: Km ⇄ Miles
- Weight: Kg ⇄ Pounds
- Temperature: °C ⇄ °F
- To-Do List: add, click-to-select, delete, clear all
- Dark theme UI (CustomTkinter)

## 📂 Structure
taskpad_unit_converter/\
│── app/\
│ └── main.py\
│── requirements.txt\
│── README.md\
│── REPORT.md\



## 🚀 Run (from source)
 
     pip install -r requirements.txt
     python app/main.py


## 📦 Build EXE (PyInstaller)

     pyinstaller app/main.py ^
       --name "TaskPad_Unit_Converter" ^
       --onefile --windowed


## 📜 License

MIT