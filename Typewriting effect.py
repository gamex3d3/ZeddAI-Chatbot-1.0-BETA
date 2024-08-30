import customtkinter as ctk
import time

# Function to create the typewriter effect
def typewriter_effect(text_widget, text, delay=100):
    def type_char(i=0):
        if i < len(text):
            text_widget.insert("end", text[i])
            text_widget.update_idletasks()
            text_widget.after(delay, type_char, i + 1)

    text_widget.delete("1.0", "end")
    type_char()

# Main window setup
root = ctk.CTk()
root.title("Typewriter Effect in Chatbot")
root.geometry("500x300")

# Label to display the typewriting effect
text_display = ctk.CTkTextbox(root, width=480, height=260)
text_display.pack(padx=10, pady=10)

# Sample text to display
sample_text = "Hello, I am your chatbot! How can I assist you today?"

# Button to start the typewriting effect
start_button = ctk.CTkButton(root, text="Start Typing", command=lambda: typewriter_effect(text_display, sample_text))
start_button.pack(pady=10)

# Run the GUI event loop
root.mainloop()
