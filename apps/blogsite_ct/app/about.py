import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw

def about_page(parent_frame, username=None, switch_page=None):
    # Clear old content
    for widget in parent_frame.winfo_children():
        widget.destroy()

    # Navbar add karna ho to
    if switch_page:
        from main import App
        App.create_navbar_static(parent_frame, username, switch_page)

    # Main background frame
    frame = ctk.CTkFrame(parent_frame, fg_color="#1a1a1a")
    frame.pack(fill="both", expand=True)

    # ===== TITLE BAR =====
    title_bar = ctk.CTkFrame(frame, fg_color="#00C9FF", corner_radius=0)
    title_bar.pack(fill="x")

    title = ctk.CTkLabel(
        title_bar,
        text="✨ About Me",
        font=("Arial", 28, "bold"),
        text_color="white"
    )
    title.pack(pady=20)

    # ===== CENTER CONTENT =====
    content = ctk.CTkFrame(frame, fg_color="#2b2b2b", corner_radius=20)
    content.pack(pady=50, padx=50, fill="both", expand=True)

    # Profile Image (Round)
    try:
        img = Image.open("assets/gallery1.jpg").resize((150, 150))
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)
        img.putalpha(mask)
        profile_img = ImageTk.PhotoImage(img)

        img_label = ctk.CTkLabel(content, image=profile_img, text="")
        img_label.image = profile_img
        img_label.pack(pady=20)

    except:
        img_label = ctk.CTkLabel(content, text="👤", font=("Arial", 80))
        img_label.pack(pady=20)

    # Bio Text
    bio = ctk.CTkLabel(
        content,
        text=(
            "Hi, I'm Agha 👋\n\n"
            "A passionate Python developer who loves creating modern\n"
            "desktop apps using CustomTkinter. This blogsite project\n"
            "is designed with a futuristic UI and smooth navigation."
        ),
        font=("Arial", 16),
        justify="center"
    )
    bio.pack(pady=10)

    # Highlight Features
    features = [
        "🚀 Modern Dark UI",
        "🖼 Stylish Photo Gallery",
        "⚡ Smooth Navigation",
        "💻 Built with Python & CustomTkinter"
    ]

    for feat in features:
        lbl = ctk.CTkLabel(content, text=feat, font=("Arial", 14))
        lbl.pack(anchor="center", pady=2)

    # Footer with neon effect
    footer = ctk.CTkLabel(
        frame,
        text="© 2025 Blogsite | Created with ❤️ by Agha",
        font=("Arial", 12),
        text_color="#00FFFF"
    )
    footer.pack(side="bottom", pady=10)
