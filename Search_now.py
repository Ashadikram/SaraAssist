import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
from gtts import gTTS
from playsound import playsound
import os

'''
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)
#print(voices[2])
engine.setProperty("rate",170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()'''
'''
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone(device_index=1) as source:
        print("Listening......")
        r.pause_threshold = 1
        r.energy_threshold = 300
        r.dynamic_energy_threshold = True
        try:
          audio = r.listen(source, timeout=5, phrase_time_limit=8)
        except Exception as e:
           print("Listninig error on search",e)
           return None

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")

    except:
        print("Say that again")
        return None
    return query'''

def speak_gtts(text):
    try:
        filename = "temp_sara.mp3"
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print("gTTS error",e)


def searchGoogle(query):
      print("google calling")
      if "google" in query:
        import wikipedia as googleScarp
        query = query.replace("sara","")
        query = query.replace("google search","")
        query = query.replace("wake up sara","")
        query = query.replace("wake up","")
        query = query.replace("sara","")
        query = query.strip()
        word_to_remove = ["google","google search", "sara", "wake up","wake up sara","search"]
        for w in word_to_remove:
            query = query.replace(w, "")
        query = query.replace("google","")
        print("Debug (cleaned query)",query)
        speak_gtts("this is what i found on google")

        try:
            pywhatkit.search(query)
            result = googleScarp.summary(query,1)
            speak_gtts(result)
        except Exception as e:
            print("NO Speakable output availabel:",e)

def searchYouTube(query):
      if "youtube" in query:
        speak_gtts("This is what i found for your search!")
        query = query.replace("youtube search","")
        query = query.replace("youtube ","")
        query = query.replace("sara","")
        query = query.replace("wake up sara","")
        query = query.replace("wake up","")
        query = query.strip()
        query = query.replace("google","")
        word_to_remove = ["youtube","youtube search", "sara", "wake up","wake up sara","search"]
        for w in word_to_remove:
            query = query.replace(w, "")
        query = query.strip()
        print("Cheaned Query", query)
        web = ("https://www.youtube.com/results?search_query=" + query)
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak_gtts("Done, Sir")

def searchWikipedia (query):
       if "wikipedia" in query:
        speak_gtts("Searching form wikipedia.......")
        query = query.replace("wikipedia","")
        query = query.replace("wake up sara","")
        query = query.replace("wake up","")
        query = query.replace("sara","")
        query = query.strip()
        query = query.replace("google","")
        query = query.replace("search wikipedia","")
        query = query.replace("sara","")
        word_to_remove = ["wikipedia","wikipedia search", "sara", "wake up","wake up sara","search"]
        for w in word_to_remove:
            query = query.replace(w, "")
        results = wikipedia.summary(query, sentences = 2)
        speak_gtts("According to wikipedia..")
        print(results)
        speak_gtts(results)








