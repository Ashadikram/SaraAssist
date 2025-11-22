import speech_recognition as sr
'''
for i , name in enumerate(sr.Microphone.list_microphone_names()):
    print(i, name)

r = sr.Recognizer()
with sr.Microphone(device_index=11) as source:
    print("Adjusting...")

r.adjust_for_ambient_noise(source,duration=1)
print("say somthing")
audio = r.listen(source, timeout=5, phrase_time_limit=4)

print("Done Listninig")

try:
    text= r.recognize_google(audio, language='en-IN')
    print("you said",text)

except Exception as e:
    print("error",e)'''

'''
def test(idx):
    print(f"\n--- Testing device_index = {idx} ---")
    r = sr.Recognizer()

    try:
        with sr.Microphone(device_index=idx) as source:
            print("Adjusting microphone...")
            r.adjust_for_ambient_noise(source, duration=1)

            print("Say something...")
            audio = r.listen(source, timeout=5, phrase_time_limit=4)

        print("Done listening!")

        text = r.recognize_google(audio, language='en-IN')
        print("You said:", text)

    except Exception as e:
        print("Error:", e)

# Test only the real microphones
for i in [1, 11]:test(i)'''

'''  r = requests.get(url)
                   data = BeautifulSoup(r.text,"html.parser")
                   temp = data.find("div", attrs= {"class": "BNeawe iBp4i AP7Wind"}).text
                   speak_gtts(f"current{search} is'''


# test_tts.py
import pyttsx3
'''
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)
engine.say("This is a test. Can you hear me?")
engine.runAndWait()
print("TTS finished")'''

'''
def speak_once(text):
    try:
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)
        engine.setProperty("rate", 170)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("TTS Error:",e) '''

import pyautogui
import time 
import os

#Voice call icon position:  Point(x=1516, y=66)
#Video call icon position Point(x=1475, y=73)
'''
print("your have 5 seconds . move mouse to Voice call icon...")
time.sleep(5)
print("Voice call icon position: ", pyautogui.position())'''


print("Now moving mouse to Video call icon in 5 seconds ..")
time.sleep(5)
print("Video icon position", pyautogui.position())

# take picture position  Point(x=659, y=884)
# video switch button positon Point(x=1555, y=397)
# video button position (x=1559, y=469)