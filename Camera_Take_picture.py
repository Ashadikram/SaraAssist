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


def take_pictures_dev(picture_type = "image"):
    #speak_gtts(f"Taking image on camera")
    pyautogui.press("super")
    time.sleep(1)
    pyautogui.typewrite("camera")
    time.sleep(1)
    pyautogui.press("enter")
    pyautogui.hotkey("ctrl","f")

    if picture_type == "image":
       speak_gtts(f"Taking picture on camera")
       pyautogui.click(x=1556, y=461)
       time.sleep(2)
       pyautogui.press("enter")
       time.sleep(5)

    elif picture_type == "video":
        speak_gtts(f"Taking video on camera")
        pyautogui.click(x=1555, y=397)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(2)

        pyautogui.click(x=1559, y=469)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(2)


''' elif picture_type == "video":
        pyautogui.click() '''