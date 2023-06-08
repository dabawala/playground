# Text to speech module. Uses pyttsx3 library.

import pyttsx3

# Create a pyttsx3 object
engine = pyttsx3.init()

# Set the rate of speech
engine.setProperty('rate', 150)

# Set the volume
engine.setProperty('volume', 0.7)

# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Say something
engine.say("The directions to tel aviv ben gurion airports are as follows:")

# Save the audio file
engine.save_to_file("Hello World!", 'read-to-user.mp3')

# Run the speech engine
engine.runAndWait()