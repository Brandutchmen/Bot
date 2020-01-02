import os, random

class Audio():

    #Music Player Interface
    playerInterface = "afplay" #Mac
    #playerInterface = "mplayer" #Raspberry Pi


    # main.py
    # audio.py
    # music/

    # voice/(accent)/insults
    # voice/(accent)/questions
    # voice/(accent)/carriers
    # voice/(accent)/enders
    # voice/(accent)/greetings


    musicDir = "music/"
    voiceDir = "voice/"
    accent = "american"

    def randomMusic():
        randomfile = random.choice(os.listdir(Audio.musicDir))
        file = Audio.musicDir + randomfile
        os.system (Audio.playerInterface + " " + file)

    def randomInsult():
        randomfile = random.choice(os.listdir(Audio.voiceDir+Audio.accent+"/insults/"))
        file = Audio.voiceDir+Audio.accent+"/insults/" + randomfile
        os.system (Audio.playerInterface + " " + file)

    def randomCarrier():
        randomfile = random.choice(os.listdir(Audio.voiceDir+Audio.accent+"/carriers/"))
        file = Audio.voiceDir+Audio.accent+"/carriers/" + randomfile
        os.system (Audio.playerInterface + " " + file)

    def randomGreeting():
        randomfile = random.choice(os.listdir(Audio.voiceDir+Audio.accent+"/greetings/"))
        file = Audio.voiceDir+Audio.accent+"/greetings/" + randomfile
        os.system (Audio.playerInterface + " " + file)

    def randomQuestion():
        randomfile = random.choice(os.listdir(Audio.voiceDir+Audio.accent+"/questions/"))
        file = Audio.voiceDir+Audio.accent+"/questions/" + randomfile
        os.system (Audio.playerInterface + " " + file)

    def randomEnder():
        randomfile = random.choice(os.listdir(Audio.voiceDir+Audio.accent+"/enders/"))
        file = Audio.voiceDir+Audio.accent+"/enders/" + randomfile
        os.system (Audio.playerInterface + " " + file)
