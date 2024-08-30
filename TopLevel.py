import customtkinter
import datetime
import wikipedia
import wolframalpha
import sys
import random
import time
from tkinter import messagebox, PhotoImage, Frame, Label
from PIL import ImageTk, Image

Username = "Admin"
app = customtkinter.CTk()


class Window1(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("ZeddAI (Enquiry Chat Library)")
        self.geometry("600x480")
        self.iconbitmap("logo1.ico")
        self.resizable(0, 0)

        # Load images
        side_img_data = Image.open("side-image.png")
        email_icon_data = Image.open("email-icon.png")
        password_icon_data = Image.open("password-icon.png")
        google_icon_data = Image.open("google-icon.png")

        self.side_img = ImageTk.PhotoImage(side_img_data)
        self.email_icon = ImageTk.PhotoImage(email_icon_data)
        self.password_icon = ImageTk.PhotoImage(password_icon_data)
        self.google_icon = ImageTk.PhotoImage(google_icon_data)

        # Create and place widgets
        side_img_bar = customtkinter.CTkLabel(master=self, text="", image=self.side_img)
        side_img_bar.pack(expand=True, side="left")

        frame = customtkinter.CTkFrame(master=self, width=300, height=480, fg_color="#ffffff")
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        welcome_back = customtkinter.CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24))
        welcome_back.pack(anchor="w", pady=(50, 5), padx=(25, 0))

        signin_text = customtkinter.CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12))
        signin_text.pack(anchor="w", padx=(25, 0))

        email_label = customtkinter.CTkLabel(master=frame, text="  Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=self.email_icon, compound="left")
        email_label.pack(anchor="w", pady=(38, 0), padx=(25, 0))

        self.email_actual = customtkinter.CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
        self.email_actual.pack(anchor="w", padx=(25, 0))

        password_title = customtkinter.CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=self.password_icon, compound="left")
        password_title.pack(anchor="w", pady=(21, 0), padx=(25, 0))

        self.password_entry = customtkinter.CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
        self.password_entry.pack(anchor="w", padx=(25, 0))

        google_button = customtkinter.CTkButton(master=frame, text="Continue With Google", fg_color="#EEEEEE", hover_color="#EEEEEE", font=("Arial Bold", 9), text_color="#601E88", width=225, image=self.google_icon)
        google_button.pack(anchor="w", pady=(35, 0), padx=(25, 0))

        login_button = customtkinter.CTkButton(master=frame, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", command=self.open_window_2, width=225)
        login_button.pack(anchor="w", pady=(15, 0), padx=(25, 0))


    def open_window_2(self):
        customtkinter.set_default_color_theme("dar k-blue")  # Themes: "blue" (standard), "green", "dark-blue"
        customtkinter.set_appearance_mode("Light")
        username = self.email_actual.get()
        password = self.password_entry.get()

        if username == "user@example.com" and password == "password":
            new_window = Window2()
            self.destroy()
            new_window.mainloop()
        else:
            messagebox.showinfo("Login failed", "Incorrect username or password.")


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x200")
        self.title("Settings")
        self.resizable(0, 0)
        self.iconbitmap(default="logo1.ico")

        self.appearance_mode_label = customtkinter.CTkLabel(self, text="Theme:", anchor="w", font=("Arial Bold", 14))
        self.appearance_mode_label.grid(row=6, column=5, padx=23, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self, values=["Dark", "Light", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=7, column=5, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self, text="UI Scaling:", anchor="w", font=("Arial Bold", 14))
        self.scaling_label.grid(row=8, column=5, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event, bg_color="transparent", fg_color=("dark gray"), text_color="white")
        self.scaling_optionemenu.grid(row=9, column=5, padx=20, pady=(10, 20))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        self.iconbitmap(default="logo1.ico")
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        self.iconbitmap(default="logo1.ico")
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


class Window2(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
        customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"

        # configure window
        self.title("ZeddAI(Educational Chatbot Library)")
        self.geometry(f"{1100}x{580}")
        self.iconbitmap("logo1.ico")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=1)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="✨ ZeddAI", font=("Arial bold", 24))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_user = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text=Username, text_color=("gray10", "#DCE4EE"), border_width=2, fg_color="transparent", hover_color="gray10")
        self.sidebar_button_user.grid(row=1, column=0, padx=20, pady=10)
        self.button_settings = customtkinter.CTkButton(self.sidebar_frame, text="⚙️ Settings", fg_color="transparent", border_width=0, text_color=("gray10", "#DCE4EE"), command=self.open_toplevel, hover_color="gray10")
        self.button_settings.grid(row=6, column=0, padx=20, pady=20)

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter a prompt")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.entry.focus()
        self.entry.bind("<Return>", self.Enter_pressed)

        self.main_button_1 = customtkinter.CTkButton(text="Send", master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), hover_color="gray", command=lambda: self.Enter_pressed(None))
        self.main_button_1.grid(row=3, column=3, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.main_button_1.focus()

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=1100, height=580, font=customtkinter.CTkFont(family="Segoe UI Variable", size=14, weight="normal", underline=False), activate_scrollbars=True)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), columnspan=3, sticky="nsew")
        self.textbox.configure(state="normal")

        # Display welcome message
        self.create_speech_bubble("Welcome to ZeddAI! How can I assist you today?", False)

    def open_toplevel(self):
        ToplevelWindow()

    def sidebar_button_event(self):
        # Handle sidebar button click event
        pass

    def Enter_pressed(self, event):
        inpeut = customtkinter.StringVar()
        text = self.entry.get()
        converted_text = self.to_lower(text)
        input_get = converted_text
        inpeut.set('')
        
        # Clear the text entry
        self.entry.delete(0, customtkinter.END)

        # Display user input with typewriting effect
        self.create_speech_bubble(f"You: {input_get}", True)
        
        # Determine response based on input
        response = ""
        if 'date' in input_get:
            response = f"The date is {datetime.datetime.now():%A, %B %d, %Y}"
        elif 'time' in input_get:
            response = f"The time is {datetime.datetime.now():%I %M %p}"
        elif 'what are the features' in input_get:
            response = (
                "These are the features:\n\n"
                "6. Date and Time (Offline)\n"
                "5. Search (Online)\n"
                "4. Summarize (Online)\n"
                "3. Calculate (Online)\n"
                "2. Who is (Online)\n"
                "1. Artificial Intelligence (Offline)\n\n"
                "These are the basic things I can do.\n"
            )
        elif 'search' in input_get:
            try:
                In = input_get.replace("search", " ")
                wikie = wikipedia.summary(In, sentences=10000000000)
                response = wikie
            except:
                response = 'Reconnecting to Wi-Fi....'
        elif 'summarize' in input_get:
            try:
                In = input_get.replace("summarize", " ")
                wikies = wikipedia.summary(In, sentences=1000)
                response = wikies
            except:
                response = 'Reconnecting to Wi-Fi....'
        elif 'who is' in input_get:
            try:
                human = input_get.replace('who is', " ")
                info = wikipedia.summary(human, sentences=10000)
                response = info
            except:
                response = 'Reconnecting to Wi-Fi....'
        elif 'who are you' in input_get:
            response = "I'm your Enquiry Chat Library(ECL), ZeddAI!"
        elif "calculate" in input_get or "what is" in input_get:
            try:
                question = input_get
                answer = self.computational_intelligence(question)
                response = answer
            except:
                response = 'Reconnecting to Wi-Fi...'
        elif 'bye' in input_get or 'goodbye' in input_get:
            response = random.choice(["bye", "goodbye", "Ok"]) + "\nI hope you learnt something new!\nHave a good day!"
            time.sleep(3)
            sys.exit()
        else:
            try:
                In = input_get
                wikie = wikipedia.summary(In, sentences=10000000000)
                response = wikie
            except:
                response = 'Reconnecting to Wi-Fi....'

        # Display response with typewriting effect
        self.create_speech_bubble(f"AI: {response}", False)

    def typewrite_text(self, widget, text, delay=0.05):
        widget.configure(state="normal")
        widget.insert("end", text)
        widget.update_idletasks()
        time.sleep(delay)
        widget.configure(state="disabled")

    def create_speech_bubble(self, text, is_user):
         bubble_bg_color = "#D0E1F9" if is_user else "#A3D8F4"
         bubble_text_color = "#000000" if is_user else "#000000"

    # Insert a new line for spacing
         self.textbox.insert("end", "\n")
    
    # Insert the text
         self.textbox.insert("end", text, ("bubble",))
    
    # Apply styles
         self.textbox.tag_add("bubble", "end-2l", "end-1l")
         self.textbox.tag_configure("bubble", background=bubble_bg_color, foreground=bubble_text_color, font=("Arial", 12))
    
    # Add spacing after the bubble
         self.textbox.insert("end", "\n")
         self.textbox.see("end")


        
        # Typewrite the text in the bubble
         self.textbox.after(0, lambda: self.typewrite_text(self.textbox, text, delay=0.05))

    def to_lower(self, text):
        return text.lower()

    def computational_intelligence(self, question):
        # Placeholder for actual computation logic
        return f"Result for: {question}"


if __name__ == "__main__":
    app = Window1()
