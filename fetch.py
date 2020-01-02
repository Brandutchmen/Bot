"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
import os


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/brandonyoung/Desktop/Robot/Bot/creds.json'

def readText(filePath):
    with open(filePath) as fp:
       line = fp.readline()
       cnt = 1
       while line:
           folder = "american/enders"
           zone = "en-US"
           voice = "en-US-Wavenet-D"
           # folder = "indian/enders"
           # zone = "en-IN"
           # voice = "en-IN-Wavenet-C"
           apiCall(line.strip(), folder, zone, voice)
           #print(line.strip())
           line = fp.readline()
           cnt += 1


def apiCall(text, folder, language_code, voice_name):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code=language_code,
        name=voice_name)
    #    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)


    i = 0
    while os.path.exists("voice/" + folder + "/" + "%s.mp3" % i):
        i += 1

    # The response's audio_content is binary.

    with open("voice/" + folder + "/" + "%s.mp3" % i, 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print("Audio content written to file "+"voice/" + folder + "/" + "%s.mp3" % i)


# folder = "american/carriers"
# zone = "en-US"
# voice = "en-US-Wavenet-D"

folder = "indian/carriers"
zone = "en-IN"
voice = "en-IN-Wavenet-C"

readText("enders.txt")

#Starters


#Insults


#Ender



# Carriers
# apiCall("Hmm, interesting", folder, zone, voice)
# apiCall("That is really interesting", folder, zone, voice)
# apiCall("Go on", folder, zone, voice)
# apiCall("Please continue speaking", folder, zone, voice)
# apiCall("I am interested", folder, zone, voice)
# apiCall("I'm happy to hear that. Go on.", folder, zone, voice)
# apiCall("I'm happy to hear that.", folder, zone, voice)

# Greetings
# apiCall("Hello", folder, zone, voice)
# apiCall("Hey!", folder, zone, voice)
# apiCall("Hello there", folder, zone, voice)
# apiCall("Hi.", folder, zone, voice)
# apiCall("Hello Human.", folder, zone, voice)
# apiCall("Hey There", folder, zone, voice)
# apiCall("Hi. How are you doing?", folder, zone, voice)
# apiCall("Greetings, Human", folder, zone, voice)
