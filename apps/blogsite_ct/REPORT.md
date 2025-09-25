# Blogsite_CT — Technical Report

## 1. Overview
Blogsite_CT is a desktop application that simulates a modern blogsite experience.  
Users can login or signup, browse blogs, view a gallery of images, and read about the creator.

## 2. Objectives
- Provide a multipage navigation experience
- Demonstrate modern UI design with CustomTkinter
- Handle images and layouts professionally
- Package into a single EXE for easy use

## 3. Architecture
- **UI Framework:** CustomTkinter
- **Image Handling:** Pillow
- **Modules:**
  - `main.py` → app entry, login/signup, navigation, home
  - `blog.py` → blog posts
  - `gallery.py` → photo gallery
  - `about.py` → about page
- **Assets:** all UI images are stored in `/assets`

## 4. Workflow
1. User logs in (or signs up).
2. Navigation bar allows switching between Home, Blog, Gallery, About.
3. Blog shows posts with image + title.
4. Gallery shows neon-bordered scrollable images.
5. About shows profile + bio + highlights.

## 5. Build Process
 
      pip install -r requirements.txt
      pyinstaller app/main.py ^
        --name "Blogsite_CT" ^
        --onefile --windowed ^
        --add-data "app/assets;assets"




## 6. Testing & Validation

Navigation works across pages

Images load correctly

Gallery scroll tested

About page profile loads

Works on Windows 10/11

## 7. Limitations

Static blog content (not editable)

Assets must remain packaged

Windows build only (default)

## 8. Future Work

Add real blog editor

Add user database

Add image uploader in gallery

Cross-platform packaging

## 9. Conclusion

Blogsite_CT demonstrates how to create a multi-page desktop GUI app with professional UI, image handling, and smooth navigation using Python.


