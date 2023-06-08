# Text to speech module. Uses pyttsx3 library.

import pyttsx3

engine = pyttsx3.init()

# Set the rate of speech
engine.setProperty('rate', 150)

# Set the volume
engine.setProperty('volume', 0.7)

# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def say(text):
    engine.say(text)
    engine.runAndWait()
