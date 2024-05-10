import os
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
import pyttsx3

# Create the main Tkinter window
root = tk.Tk()
root.title("Text-to-Speech Converter")

# Function to convert text to speech and play
def convert_and_play():
    text_to_speech = entry.get()
    if text_to_speech:
        try:
            # Initialize the text-to-speech engine
            engine = pyttsx3.init()

            # Set properties (optional)
            # engine.setProperty('rate', 150)  # Speed of speech

            # Convert text to speech and play
            engine.say(text_to_speech)
            engine.runAndWait()

        except Exception as e:
            messagebox.showerror("Error","Error playing speech: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter some text.")

# Create GUI elements
label = Label(root, text="Enter text to convert:")
label.pack(pady=10)

entry = Entry(root, width=50)
entry.pack(pady=10)

convert_button = Button(root, text="Convert and Play", command=convert_and_play)
convert_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
