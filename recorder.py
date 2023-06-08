# This file is used to record a short audio file and then transcribe it using the Rev.ai API
# A graphical button is used to start the recording, and the recording stops when the button
# is released. The audio file is saved in the same directory as the python file.
# The audio file is then transcribed using the Rev.ai API.
# The graphical button is created using the tkinter library.
# We also gonna implement the entire window using tkinter.

import tkinter as tk # used to create graphical button
from tkinter import ttk as ttk
import pyaudio # used to record audio
import wave # used to save audio
import os # used to delete audio file
from rev_ai import apiclient # used to transcribe audio
from rev_ai.models.asynchronous.job_status import JobStatus # used to check if audio has been transcribed
import time # used to wait for audio to be transcribed

# Create event handler for rec_btn button:
def record(event):
    # Create a pyaudio object
    p = pyaudio.PyAudio()
    # Create a stream
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    # Create a list to store the audio data
    frames = []
    # keep recording as long as the button is pressed
    while event.widget.instate(['pressed']):
        data = stream.read(1024)
        frames.append(data)
    # stop recording
    stream.stop_stream()
    stream.close()
    p.terminate()
    # save the audio file in mp3 format
    wf = wave.open('testi.mp3', 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()
    # create a window to display "recording done"
    root2 = tk.Tk()
    frm2 = ttk.Frame(root2, padding=10)
    frm2.grid()
    ttk.Label(frm2, text="Recording done").grid(column=0, row=0)
    root2.mainloop()

# Create a window
root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Please press to record").grid(column=0, row=0)
# create a button to record audio. as long as the button is pressed, audio is recorded
rec_btn = ttk.Button(frm, text="Record")
rec_btn.grid(column=0, row=1)
rec_btn.bind("<ButtonPress>", record)
root.mainloop()

# Create event handler for rec_btn button:
def record():
    pass