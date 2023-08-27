import speech_recognition as sr
import subprocess
import keyboard
import time

class VoiceRec():

    def getVoiceText(self):
        r=sr.Recognizer()
        mic = sr.Microphone()

        print("Chargement...")
        time.sleep(2)
        print("commande vocal active...")

        with mic as source:
            audio = r.listen(source)

        voiceText = r.recognize_google(audio)

        print("Fin detection vocal")
            
        return voiceText