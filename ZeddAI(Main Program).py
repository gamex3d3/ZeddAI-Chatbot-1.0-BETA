import customtkinter
import datetime
import wikipedia
import wolframalpha
import sys
import random
import time
from tkinter import messagebox, PhotoImage
from PIL import ImageTk, Image

Username = "Admin"
app = customtkinter.CTk()

class Window1(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("ZeddAI(Enquiry Chat Library)")
        self.geometry("600x480")
        self.iconbitmap("logo1.ico")
        self.resizable(0,0)

        self.welcome_back = customtkinter.CTkLabel(
            master=self,
            text="Welcome Back!",
            text_color="#601E88",
            anchor="w",
            justify="left",
            font=("Arial Bold", 24)
        )
        self.welcome_back.grid(pady=(50, 5), padx=(25, 0))

        self.signin_text = customtkinter.CTkLabel(
            master=self,
            text="Sign in to your account",
            text_color="#7E7E7E",
            anchor="w",
            justify="left",
            font=("Arial Bold", 12)
        )
        self.signin_text.grid(padx=(25, 0))

        self.email_label = customtkinter.CTkLabel(
            master=self,
            text="  Email:",
            text_color="#601E88",
            anchor="w",
            justify="left",
            font=("Arial Bold", 14),
            compound="left"
        )
        self.email_label.grid(pady=(38, 0), padx=(25, 0))

        self.email_actual = customtkinter.CTkEntry(
            master=self,
            width=225,
            fg_color="#EEEEEE",
            border_color="#601E88",
            border_width=1,
            text_color="#000000"
        )
        self.email_actual.grid(padx=(25, 0))

        self.password_title = customtkinter.CTkLabel(
            master=self,
            text="  Password:",
            text_color="#601E88",
            anchor="w",
            justify="left",
            font=("Arial Bold", 14),
            compound="left"
        )
        self.password_title.grid(pady=(21, 0), padx=(25, 0))

        self.password_entry = customtkinter.CTkEntry(
            master=self,
            width=225,
            fg_color="#EEEEEE",
            border_width=1,
            show="*"
        )
        self.password_entry.grid(padx=(25, 0))

        self.login_button = customtkinter.CTkButton(
            master=self, 
            text="Login", 
            fg_color="#601E88", 
            hover_color="#E44982", 
            font=("Arial Bold", 12), 
            text_color="#ffffff", 
            width=225,
            command=self.open_window_2
        )
        self.login_button.grid(pady=(40, 0), padx=(25, 0))

        self.google_button = customtkinter.CTkButton(
            master=self, 
            text="Continue With Google", 
            fg_color="#601E88", 
            hover_color="#E44982", 
            font=("Arial Bold", 9), 
            text_color="#ffffff", 
            width=225, 
        )
        self.google_button.grid(pady=(20, 0), padx=(25, 0))
       
        self.mainloop()

    def open_window_2(self):
        customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
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
        self.resizable(0,0)
        self.iconbitmap(default="logo1.ico")
        
        self.appearance_mode_label = customtkinter.CTkLabel(self, text="Theme:", anchor="w", font=("Arial Bold", 14))
        self.appearance_mode_label.grid(row=6, column=5, padx=23, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self, values=["Dark", "Light", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=7, column=5, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self, text="UI Scaling:", anchor="w", font=("Arial Bold", 14))
        self.scaling_label.grid(row=8, column=5, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event,bg_color="transparent", fg_color=("dark gray"), text_color="white")
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

        self.sidebar_button_user = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text= Username, text_color=("gray10", "#DCE4EE"), border_width=2, fg_color="transparent",  hover_color="gray10")
        self.sidebar_button_user.grid(row=1, column=0, padx=20, pady=10)
        self.button_settings = customtkinter.CTkButton(self.sidebar_frame, text="⚙️ Settings",fg_color="transparent", border_width=0, text_color=("gray10", "#DCE4EE"),command=self.open_toplevel, hover_color="gray10")
        self.button_settings.grid(row=6, column= 0, padx=20, pady=20)

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter a prompt")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.entry.focus()
        self.entry.bind("<Return>", self.Enter_pressed)

        self.main_button_1 = customtkinter.CTkButton(text="Send", master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), hover_color="gray", command=lambda: self.Enter_pressed(None))
        self.main_button_1.grid(row=3, column=3,columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew" )
        self.main_button_1.focus()

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=1100, height=580, font=customtkinter.CTkFont(family= "Segoe UI Variable" ,size=14, weight="normal", underline=False), activate_scrollbars=True)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
    def typewrite_text(self, widget, text, delay=0.02):
        for char in text:
            widget.insert("end", char)
            widget.update_idletasks()
            time.sleep(delay)
        widget.insert("end", "\n\n")
        
    def computational_intelligence(self, question):
        app_id = "7E8RXT-5E8UJ7K2AX"
        try:
            client = wolframalpha.Client(app_id)
            answer = client.query(question)
            answer = next(answer.results).text
            return answer
        except:
            print("Reconnecting...")
        return None
    
    def to_lower(self, text):
        """Converts a string to lowercase.

        Args:
            text: A string representing the text to convert.

        Returns:
        A string representing the converted text in lowercase.
            """
        return text.lower() 

    def Enter_pressed(self, event):
        inpeut = customtkinter.StringVar()
        text = self.entry.get()
        converted_text = self.to_lower(text)
        input_get = converted_text
        print(input_get)
        inpeut.set('')
        
        self.textbox.insert("end", f"You: {input_get}\n\n")
        
        if 'date' in input_get:
            self.typewrite_text(self.textbox, "AI: The date is " + f"{datetime.datetime.now():%A, %B %d, %Y}")
    

        elif 'time' in input_get:
            self.typewrite_text(self.textbox, "AI: The time is " + f"{datetime.datetime.now():%I %M %p}")
            
        
        elif 'what are the features' in input_get:
            features_text = (
                "This are the basic things I can do:\n"
                "1. Enquiry Chat Library\n\n"
                "2. Who is (Online)\n"
                "3. Calculate (Online)\n"
                "4. Summarize (Online)\n"
                "5. Search (Online)\n"
                "6. Date and Time (Offline)\n"
                "AI: This are also keywords if you want to give any prompt. For Example: Summarize Romeo and Julliet, Who is Nelson Mandela?\n\n"
                
            )
            self.typewrite_text(self.textbox, features_text)
            
        elif 'search' in input_get:
            try:
                In = input_get.replace("search", " ")
                wikie = wikipedia.summary(In, sentences = 10000)
                self.typewrite_text(self.textbox, "AI: " + wikie)
            except:
                self.typewrite_text(self.textbox, 'AI: Reconnecting to Wi-Fi....')
    
        elif 'summarize' in input_get:
            try:
                In = input_get.replace("summarize", " ")
                wikies = wikipedia.summary(In, sentences = 1000)
                self.typewrite_text(self.textbox, "AI: " + wikies)
                
            except:
                 self.typewrite_text(self.textbox, 'AI: Reconnecting to Wi-Fi....')

        elif 'who is' in input_get:
            try:
                human = input_get.replace('who is', " ")
                info = wikipedia.summary(human, sentences = 1000)
                self.typewrite_text(self.textbox, "AI: " + info)
                
            except:
                self.typewrite_text(self.textbox, 'AI: Reconnecting to Wi-Fi....')
                

        elif 'who are you' in input_get:
            self.typewrite_text(self.textbox, "AI: I'm your Enquiry Chat Library(ECL), ZeddAI!")
            
            
        elif "calculate" in input_get or "what is" in input_get:
            try:
                question = input_get
                answer = self.computational_intelligence(question) 
                self.typewrite_text(self.textbox, "AI: " + answer)
                
            except:
                self.typewrite_text(self.textbox, 'AI: Reconnecting to Wi-Fi...')
                

        elif 'bye' in input_get or 'goodbye' in input_get:
            st_msgs = (
                    "bye",
                    "goodbye",
                    "Ok",
                )
            self.typewrite_text(self.textbox, "AI: " + random.choice(st_msgs))
            time.sleep(1)
            self.typewrite_text(self.textbox, "AI: I hope you learnt something new!")
            self.typewrite_text(self.textbox, "AI: Have a good day!")
            time.sleep(3)
            sys.exit()

        else:
            try:
                In = input_get
                wikie = wikipedia.summary(In, sentences = 100)
                self.typewrite_text(self.textbox, "AI: " + wikie)
            except:
                self.typewrite_text(self.textbox, 'AI: Reconnecting to Wi-Fi....')

        self.entry.delete(0, customtkinter.END)
    
    def sidebar_button_event(self):
        self.typewrite_text(self.textbox, "CREDIT: C^2 2024© All rights reserved.")
        print("Account Button Clicked")

        
    def open_toplevel(self):
        self.iconbitmap("logo1.ico")
        self.toplevel_window = None
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
        print("Settings Button Clicked")

if __name__ == "__main__":
    app = Window1()
    app.mainloop()
