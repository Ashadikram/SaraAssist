import pywhatkit
import pyttsx3
import speech_recognition
import webbrowser
import datetime
from gtts import gTTS
from playsound import playsound
import os
from bs4 import BeautifulSoup
from time import sleep
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)
#print(voices[2])
engine.setProperty("rate",170)

def speak_gtts(text):
    try:
        filename = "temp_sara.mp3"
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print("gTTS error",e)

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone(device_index=1) as source:
        print("Listening......")
        r.pause_threshold = 1
        r.energy_threshold = 300
        r.dynamic_energy_threshold = True
        r.phrase_threshold = 0.3
        r.non_speaking_duration = 0.6

        try:
           audio = r.listen(source, timeout=1, phrase_time_limit=7)
        except Exception as e:
            print("Listning error",e)
            return None

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")

    except:
        print("Say that again")
        return None
    return query

strtime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes=2)).strftime("%M"))

def sendMessage():
    speak_gtts("who do you want to send message to ?")
    speak_gtts('''My Brother press 1 : , Arshad clg press 2: , Zaid press 3: ''')
    a = takeCommand()
   # a = int(input("Enter your Choice"))
    if a == 1 or a == str("My Brother") or a == str("brother") or a == str("ashad") or a == str("Brother"):
        speak_gtts("what is the message ?")
        #message =  int(input("Enter your message: "))
        message = takeCommand()
        pywhatkit.sendwhatmsg("+917253908831",message, time_hour=(strtime), time_min=update)
    elif a == 2:
        pass
