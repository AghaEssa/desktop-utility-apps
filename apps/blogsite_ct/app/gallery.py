import customtkinter as ctk
from PIL import Image, ImageTk, ImageOps, ImageDraw
import os

def gallery_page(parent_frame, username, switch_page):
    # Purana content clear
    for widget in parent_frame.winfo_children():
        widget.destroy()

    # Navbar add karo
    from main import App
    App.create_navbar_static(parent_frame, username, switch_page)

    # Main content frame
    frame = ctk.CTkFrame(parent_frame, fg_color="#2b2b2b")
    frame.pack(fill="both", expand=True)

    # Title
    title = ctk.CTkLabel(frame, text="🖼 Photo Gallery", font=("Arial", 24, "bold"))
    title.pack(pady=20)

    # Scrollable canvas
    canvas = ctk.CTkCanvas(frame, bg="#2b2b2b", highlightthickness=0)
    scrollbar = ctk.CTkScrollbar(frame, orientation="vertical", command=canvas.yview)

    scroll_frame = ctk.CTkFrame(canvas, fg_color="#2b2b2b")
    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Column config -> Centering
    for i in range(3):  # 3 images per row
        scroll_frame.grid_columnconfigure(i, weight=1)





    # Images load karna
    image_folder = "assets"
    images = [
        "gallery1.jpg", "gallery2.jpg", "church.jpg", "meeting.jpg", "blog.jpg",
        "gallery3.jpg", "gallery4.jpg", "gallery5.jpg", "gallery6.jpg", "gallery7.jpg",
        "gallery8.jpg", "gallery9.jpg", "gallery10.jpg", "gallery11.jpg", "gallery12.jpg",
        "gallery13.jpg", "gallery14.jpg", "gallery15.jpg", "gallery16.jpg"
    ]

    # Column config -> Centering
    for i in range(3):  # 3 images per row
        scroll_frame.grid_columnconfigure(i, weight=1)


    row, col = 0, 0
    for img_name in images:
        try:
            img_path = os.path.join(image_folder, img_name)
            img = Image.open(img_path).resize((250, 180))

            # Round corners (mask)
            mask = Image.new("L", img.size, 0)
            mask_draw = ImageDraw.Draw(mask)
            mask_draw.rounded_rectangle([(0, 0), img.size], radius=30, fill=255)
            img.putalpha(mask)

            # Border with rounded mask (transparent + neon)
            border_size = 8
            bordered = Image.new("RGBA", (img.size[0] + border_size * 2, img.size[1] + border_size * 2), (0, 0, 0, 0))

            # neon rectangle background
            neon_rect = Image.new("RGBA", bordered.size, (0, 255, 255, 255))
            neon_mask = Image.new("L", bordered.size, 0)
            neon_draw = ImageDraw.Draw(neon_mask)
            neon_draw.rounded_rectangle(
                [(0, 0), bordered.size],
                radius=38,  # 30 + 8 border
                fill=255
            )
            bordered.paste(neon_rect, (0, 0), neon_mask)

            # paste image at center
            bordered.paste(img, (border_size, border_size), img)

            photo = ImageTk.PhotoImage(bordered)

            # Label center align
            lbl = ctk.CTkLabel(scroll_frame, image=photo, text="")
            lbl.image = photo
            lbl.grid(row=row, column=col, padx=30, pady=30, sticky="nsew")

            col += 1
            if col > 2:  # 3 per row
                col = 0
                row += 1

        except Exception as e:
            pass

    for i in range(3):  # 3 columns
        scroll_frame.grid_columnconfigure(i, weight=1)
        scroll_frame.grid_rowconfigure(row, weight=1)

