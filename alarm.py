import pyttsx3
import datetime
import os
import pyautogui
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import os

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

extractedtime = open("alarm.txt","rt")
time = extractedtime.read()
Time = str(time).replace("set alarm for","").strip()
extractedtime.close()

deletetime = open("alarm.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("sara","")
    timenow = timeset.replace("set alarm","")
    timenow = timeset.replace(" and ",":")

    Alarmtime = str(timenow).strip()
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak_gtts("wake up sir! its time to get up")
            os.startfile("wake_up.mp3")

        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(Time)  



