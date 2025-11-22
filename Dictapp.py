import pyautogui
import webbrowser
import pyttsx3
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


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"command prompt":"cmd",
           "paint":"mspaint",
           "word":"winword",
           "excel":"excel",
           "chrome":"chrome",
           "vscode":"code",
           "powerpoint":"powerpnt",
           "camera":"start microsoft.windows.camera:",
           "calculator":"calc",
           "notepad":"notepad"}

def openappweb(query):
    query = query.lower()
    speak_gtts("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        site = query.replace("open","").replace("launch","").strip()
        query = query.replace("open","")
        query = query.replace("sara","")
        query = query.replace("launch","")
        query = query.replace("","")

        webbrowser.open(f"https://www.{site}")
        return

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                if app == "camera":
                    os.system(f"start {dictapp[app]}")
                
                os.system(f"start {dictapp[app]}")
                return
        speak_gtts("Sorry sir, I cannot open that")

def closeappweb(query):
    speak_gtts("Clossing , sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak_gtts("all tabs are closed")

    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak_gtts("all tabs closed")


    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak_gtts("all tabs closed")

    
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak_gtts("all tabs closed")


    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak_gtts("all tabs closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")




