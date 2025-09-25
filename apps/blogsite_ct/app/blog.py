import customtkinter as ctk
from PIL import Image, ImageTk
import os


def blog_page(parent_frame, username, switch_page):
    # Clear previous widgets
    for widget in parent_frame.winfo_children():
        widget.destroy()

    # Navbar add karo
    from main import App  # circular import avoid karna hoga
    App.create_navbar_static(parent_frame, username, switch_page)

    # Main frame
    frame = ctk.CTkFrame(parent_frame, fg_color="#2b2b2b")
    frame.pack(fill="both", expand=True)

    # Title
    title = ctk.CTkLabel(frame, text="Our Blog Articles", font=("Arial", 28, "bold"))
    title.pack(pady=20)

    # Container for posts
    container = ctk.CTkFrame(frame, fg_color="#2b2b2b")
    container.pack(pady=10, fill="both", expand=True)

    # Blog posts (image + title)
    image_folder = "assets"
    posts = [
        ("meeting.jpg", "Remote Collaboration"),
        ("blog.jpg", "Content Development"),
        ("church.jpg", "Visual Storytelling"),
    ]

    for img_name, blog_title in posts:
        card = ctk.CTkFrame(container, fg_color="#1e1e1e", corner_radius=15, width=600, height=150)
        card.pack(pady=15, padx=20)

        # Image
        try:
            img = Image.open(os.path.join(image_folder, img_name)).resize((200, 120))
            photo = ImageTk.PhotoImage(img)

            img_label = ctk.CTkLabel(card, image=photo, text="")
            img_label.image = photo  # prevent garbage collection
            img_label.place(relx=0.05, rely=0.5, anchor="w")

        except:
            img_label = ctk.CTkLabel(card, text="[Image Missing]", font=("Arial", 14))
            img_label.place(relx=0.05, rely=0.5, anchor="w")

        # Blog Title
        text_label = ctk.CTkLabel(card, text=blog_title, font=("Arial", 18, "bold"))
        text_label.place(relx=0.4, rely=0.5, anchor="w")