import pyttsx3
import datetime
import playsound
from gtts import gTTS
import time
import os
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)
#print(voices[2])
engine.setProperty("rate",170)
'''
def speak_gtts(text):
    try:
        filename = "temp_sara.mp3"
        tts = gTTS(text=text, lang='en-in')
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print("gTTS error",e)'''

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning, sir")
        time.sleep(1)
        speak("what i can help you today")

    elif hour > 12 and hour <=18:
        speak("Good Afternoon, sir")
        #time.sleep(1)
        speak("what i can help you today")
        


    else:
    
        speak("Good Evening, sir")
        time.sleep(1)
        speak("what i can help you today")

    speak("Please tell me , how canI help you ?")
    