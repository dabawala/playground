#!/usr/bin/env python3

from transcriber import Transcriber
from evaluator import get_full_response_for_input
from tts import say

t = Transcriber(
    on_finish=lambda transcript: say(get_full_response_for_input(transcript)),
    on_error=lambda reason: say(f"Error: {reason}"),
)

def transcriber_toggle(event):
    if t.is_recording:
        print("Stopped recording")
        t.stop()
    else:
        print("Started recording")
        t.start()

import tkinter as tk # used to create graphical button
from tkinter import ttk as ttk

# Create a window
root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Please press to record").grid(column=0, row=0)
# create a button to record audio. as long as the button is pressed, audio is recorded
rec_btn = ttk.Button(frm, text="Record")
rec_btn.grid(column=0, row=1)
rec_btn.bind("<ButtonPress>", transcriber_toggle)
root.mainloop()
