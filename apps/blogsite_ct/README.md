# 🌐 Blogsite_CT

A modern **desktop blogsite application** built with **Python (CustomTkinter + Pillow)**.  
Includes login/signup flow, a home dashboard, a blog page, a stylish gallery with neon borders, and an about page with profile + bio.

## ✨ Features
- Login & Signup pages
- Custom navigation bar
- Blog posts with images
- Scrollable photo gallery with neon frame
- About page with profile image and bio
- Modern dark UI theme

## 📂 Project Structure
blogsite_ct/\
│── app/\
│ ├── main.py # App entrypoint\
│ ├── blog.py # Blog posts UI\
│ ├── gallery.py # Photo gallery\
│ ├── about.py # About page\
│ └── assets/ # Images used in blog & gallery\
│── requirements.txt\
│── README.md\
│── REPORT.md\




## 🚀 Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2 Run the app:

     python app/main.py


3  Build Executable    

      pyinstaller app/main.py ^
     --name "Blogsite_CT" ^
     --onefile --windowed ^
     --add-data "app/assets;assets"
📜 License

MIT