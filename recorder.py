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
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 3
    filename = "output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    # create a window to display "recording done"

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
