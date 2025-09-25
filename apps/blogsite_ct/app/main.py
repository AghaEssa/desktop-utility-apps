import customtkinter as ctk
import blog
import gallery
import about

ctk.set_appearance_mode("dark")  # dark/light/system
ctk.set_default_color_theme("dark-blue")  # themes: blue, green, dark-blue

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Blogsite_CT - Agha")
        self.geometry("1000x700")

        # container frame
        self.container = ctk.CTkFrame(self, fg_color="#2b2b2b")
        self.container.pack(fill="both", expand=True)

        # Start with login page
        self.show_login_page()


    def clear_frame(self):
        for widget in self.container.winfo_children():
            widget.destroy()



    def switch_page(self, page_name):
        self.clear_frame()
        if page_name == "home":
            self.show_home(self.username)
        elif page_name == "blog":
            blog.blog_page(self.container, self.username, self.switch_page)
        elif page_name == "gallery":
            gallery.gallery_page(self.container, self.username, self.switch_page)
        elif page_name == "about":
            about.about_page(self.container, self.username, self.switch_page)

    @staticmethod
    def create_navbar_static(parent, username, switch_page):
        header = ctk.CTkFrame(parent, height=60, fg_color="#005f99")
        header.pack(fill="x", side="top")

        welcome = ctk.CTkLabel(
            header,
            text=f"🌐 Welcome, {username}",
            font=("Arial", 20, "bold"),
            text_color="white"
        )
        welcome.pack(side="left", padx=25, pady=10)

        btn_frame = ctk.CTkFrame(header, fg_color="#005f99")
        btn_frame.pack(side="right", padx=25)

        nav_btn_style = {"fg_color": "#0088cc", "hover_color": "#00aaff", "font": ("Arial", 15, "bold")}

        ctk.CTkButton(btn_frame, text="🏠 Home",
                      command=lambda: switch_page("home"), **nav_btn_style).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="📝 Blog",
                      command=lambda: switch_page("blog"), **nav_btn_style).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="🖼 Gallery",
                      command=lambda: switch_page("gallery"), **nav_btn_style).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="ℹ About",
                      command=lambda: switch_page("about"), **nav_btn_style).pack(side="left", padx=10)

    # -------------------- NAVBAR --------------------
    def create_navbar(self, parent, username):
        header = ctk.CTkFrame(parent, height=60, fg_color="#005f99")  # height badi + new color
        header.pack(fill="x", side="top")

        welcome = ctk.CTkLabel(
            header,
            text=f"🌐 Welcome, {username}",
            font=("Arial", 20, "bold"),
            text_color="white"
        )
        welcome.pack(side="left", padx=25, pady=10)

        btn_frame = ctk.CTkFrame(header, fg_color="#005f99")
        btn_frame.pack(side="right", padx=25)

        nav_btn_style = {"fg_color": "#0088cc", "hover_color": "#00aaff", "font": ("Arial", 15, "bold")}

        ctk.CTkButton(btn_frame, text="🏠 Home",
                      command=lambda: self.switch_page("home"), **nav_btn_style).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="📝 Blog",
                      command=lambda: self.switch_page("blog"), **nav_btn_style).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="🖼 Gallery",
                      command=lambda: self.switch_page("gallery"), **nav_btn_style).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="ℹ About",
                      command=lambda: self.switch_page("about"), **nav_btn_style).pack(side="left", padx=10)



    # -------------------- LOGIN PAGE --------------------
    def show_login_page(self):
        self.clear_frame()

        frame = ctk.CTkFrame(self.container)
        frame.pack(expand=True)

        title = ctk.CTkLabel(frame, text="Login", font=("Arial", 40, "bold"))
        title.pack(pady=30,padx=70)

        username_entry = ctk.CTkEntry(frame, placeholder_text="Username", width=200)
        username_entry.pack(pady=10, padx=70)

        password_entry = ctk.CTkEntry(frame, placeholder_text="Password", show="*", width=200)
        password_entry.pack(pady=10, padx=70)

        def login():
            username = username_entry.get()
            if username.strip():
                self.show_home(username)

        login_btn = ctk.CTkButton(frame, text="Login", command=login)
        login_btn.pack(pady=20,padx=70)

        switch_btn = ctk.CTkButton(frame, text="No account? Signup",
                                   fg_color="transparent", command=self.show_signup_page)
        switch_btn.pack(pady=20,padx=70)




    # -------------------- SIGNUP PAGE --------------------
    def show_signup_page(self):
        self.clear_frame()

        frame = ctk.CTkFrame(self.container)
        frame.pack(expand=True)

        title = ctk.CTkLabel(frame, text="Signup", font=("Arial", 30, "bold"))
        title.pack(pady=20, padx=70)

        username_entry = ctk.CTkEntry(frame, placeholder_text="New Username", width=200)
        username_entry.pack(pady=10, padx=70)

        password_entry = ctk.CTkEntry(frame, placeholder_text="New Password", show="*", width=200)
        password_entry.pack(pady=10, padx=70)

        def signup():
            username = username_entry.get()
            if username.strip():
                self.show_home(username)

        signup_btn = ctk.CTkButton(frame, text="Signup", command=signup)
        signup_btn.pack(pady=20, padx=70)

        switch_btn = ctk.CTkButton(frame, text="Have account? Login",
                                   fg_color="transparent", command=self.show_login_page)
        switch_btn.pack(pady=20, padx=70)

    # -------------------- HOME PAGE --------------------
    def show_home(self, username):
        self.username = username
        self.clear_frame()

        # Navbar
        self.create_navbar(self.container, username)

        # Body
        body = ctk.CTkFrame(self.container, fg_color="#1e1e1e")
        body.pack(fill="both", expand=True)

        # Card style box in center
        card = ctk.CTkFrame(body, fg_color="#2d2d2d", corner_radius=20)
        card = ctk.CTkFrame(body, fg_color="#1e1e1e", corner_radius=15, width=600, height=300)
        card.place(relx=0.5, rely=0.5, anchor="center")

        title = ctk.CTkLabel(card, text="🚀 Blogsite_CT",
                             font=("Arial", 30, "bold"), text_color="white")
        title.pack(pady=(40, 10))

        desc = ctk.CTkLabel(card,
                            text="A modern blogsite where you can explore blogs, gallery, and learn more about us.\n"
                                 "Built with CustomTkinter ✨",
                            font=("Arial", 16), text_color="#bbbbbb", justify="center")
        desc.pack(pady=10)

        ctk.CTkButton(card, text="Get Started", fg_color="#00aaff", hover_color="#33bbff",
                      font=("Arial", 15, "bold")).pack(pady=20)




if __name__ == "__main__":
    app = App()
    app.mainloop()
