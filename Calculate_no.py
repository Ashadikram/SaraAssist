import wolframalpha
import pyttsx3
import speech_recognition 
import time
from gtts import gTTS
from playsound import playsound
import os
import requests
import json

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


def WolfRamAlpha(query):
   try:
       query = query.replace(" ","")
       api_key = "6GAV55TTKR"
       #url = f"http://api.wolframalpha.com/v1/result?i=5+6&appid=YOUR_KEY"
       #url = f"http://api.wolframalpha.com/v2/query?input=QUERY&appid=KEY&output=json"
       url = f"http://api.wolframalpha.com/v2/query?input={query}&appid={api_key}&output=json"
       print("url im using",url)
       res = requests.get(url)

       if res.status_code != 200:
           speak_gtts("sorry sir, i am unable to do the calculation")
           return None
       
       data = res.json()
       pods = data["queryresult"].get("pods",[])
       for pod in pods:
           if pod["title"] in ["Result","Exact result", "Decimal approximation"]:
               answer = pod['subpods'][0]['plaintext']
               speak_gtts(f"sir, the result is {answer}")
               return answer
           
       if pods:
           answer = pods[0]["subpods"][0]["plaintext"]
           speak_gtts(f"sir, the result is {answer}")
           return answer
       speak_gtts("sorry sir , i could not find the result")


   except Exception as e:
       speak_gtts("Sorry sir , value not found")
       print("Error: ",e )
       return None


def calc(query):
    Term = str(query)
    Term = Term.replace("calculate","")
    Term = Term.replace("sara","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("divide","/")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"result is {result}")
        speak_gtts(f"sir, the result is {result}")

    except:
        speak_gtts("sorry sir, I am unable to do the calculation")


