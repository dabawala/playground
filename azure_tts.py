import azure.cognitiveservices.speech as speech
import os

# Set up the speech config
speech_key = 'f844b728b0cb4c889e9d32cdf24647f9'
service_region = 'eastus'
speech_config = speech.SpeechConfig(subscription=speech_key, region=service_region)
synthesizer = speech.SpeechSynthesizer(speech_config=speech_config)

def say(text_to_speak):
    result = synthesizer.speak_text_async(text_to_speak).get()
    audio_file = './tmp/azure-output.wav'
    with open(audio_file, 'wb') as file:
        file.write(result.audio_data)
    # play the audio file
    
    os.system('start ' + audio_file)
