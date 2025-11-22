import pyautogui
import webbrowser
import pyttsx3
import time
from gtts import gTTS
from playsound import playsound
import os
import speech_recognition


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


def whatsapp_call_dev(contact_name, call_type="voice"):
    speak_gtts(f"calling {contact_name} on whatsapp")
    pyautogui.press("super")
    time.sleep(1)
    pyautogui.typewrite("whatsapp")
    time.sleep(1.5)
    pyautogui.press("enter")
    time.sleep(2)

    pyautogui.hotkey("ctrl", "f")
    time.sleep(1)

    pyautogui.typewrite(contact_name)
    time.sleep(2)
    pyautogui.click(200,200)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(3)

    if call_type == "voice":
        pyautogui.click(x=1516, y=66) #voice call icon position

    elif call_type == "video":
        pyautogui.click(x=1475, y=73) #video call icon  position

    else:
        speak_gtts("Invalid call type specified")

speak_gtts("Calling now sir")
