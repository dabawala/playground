import azure.cognitiveservices.speech as speech
import os

# Set up the speech config
speech_key = 'f844b728b0cb4c889e9d32cdf24647f9'
service_region = 'eastus'
speech_config = speech.SpeechConfig(subscription=speech_key, region=service_region)

# Create the speech synthesizer
synthesizer = speech.SpeechSynthesizer(speech_config=speech_config)

# Specify the text to be synthesized
text_to_speak = 'Hello, world!'

# Synthesize speech and save it to a file
result = synthesizer.speak_text_async(text_to_speak).get()
audio_file = 'output.wav'
with open(audio_file, 'wb') as file:
    file.write(result.audio_data)

# Play the audio file
os.system('start ' + audio_file)
