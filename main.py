#!/usr/bin/env python3

from transcriber import Transcriber
from evaluator import get_full_response_for_input
from azure_tts import say
import mtranslate

import tkinter as tk # used to create graphical button
from tkinter import ttk as ttk

root = tk.Tk()
frm = ttk.Frame(root, padding=10)
rec_btn = ttk.Button(frm, text="Speak")

def say_and_print(text):
    print(text)
    say(text)

def on_finish(transcript):
    print(f"Got transcript: {transcript}")
    rec_btn["text"] = "Speak"
    rec_btn["state"] = "normal"
    say_and_print(get_full_response_for_input(transcript))

def on_error(reason):
    rec_btn["text"] = "Speak"
    # enable button again
    rec_btn["state"] = "normal"
    say_and_print(f"Error: {reason}")

t = Transcriber(on_finish, on_error)
def transcriber_toggle(event):
    if t.is_recording:
        print("Stopped recording")
        t.stop()
        # change the button text back to "Record"
        rec_btn["text"] = "Wait..."
        # disable the button until the transcription is done
        rec_btn["state"] = "disabled"
    else:
        print("Started recording")
        # change the button text to "Stop"
        rec_btn["text"] = "Stop"
        t.start()

# Create a window
frm.grid()

# 

# ttk.Label(frm, text="Please press to record").grid(column=0, row=0)
# create a button to record audio. as long as the button is pressed, audio is recorded
rec_btn.grid(column=0, row=0)
rec_btn.bind("<ButtonPress>", transcriber_toggle)
root.mainloop()
