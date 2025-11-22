import requests
import json
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


def latest_news():
    api_key = {"buisness":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=2a5408e5efcb47adb04dd4f58a36f1ec" ,
               "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=2a5408e5efcb47adb04dd4f58a36f1ec",
               "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=2a5408e5efcb47adb04dd4f58a36f1ec",
               "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=2a5408e5efcb47adb04dd4f58a36f1ec",
               "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=2a5408e5efcb47adb04dd4f58a36f1ec",
               "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=2a5408e5efcb47adb04dd4f58a36f1ec"}
                #"2a5408e5efcb47adb04dd4f58a36f1ec"

    content = None
    url = None
    speak_gtts("which category news you would like to hear. Buisness, Entertainment, Health, Science, Sports, Technology")
    field = input("enter category:")
    for key, value in api_key.items():
        if key.lower() in field.lower():
            url = value 
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
            speak_gtts("sorry sir, I am unable to find the category you mentioned. Here are some top headlines")
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=2a5408e5efcb47adb04dd4f58a36f1ec"
                
    news = requests.get(url).text
    news = json.loads(news)
    speak_gtts("here is the first top headlines")
    arts = news["articles"]
    for articles in arts:
        title = articles["title"]
        url = articles['url']
        print(title)
        speak_gtts(title)
        time.sleep(2)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to continue news ] and [ press 2 to stop news]")
        if str(a) == "1":
            continue
        elif str(a) == "2":
            speak_gtts("thanks for listening sir, have a nice day")
            break

        speak_gtts("that was all for today sir, have a nice day")

