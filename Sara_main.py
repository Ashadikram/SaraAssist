import pyttsx3
import speech_recognition
import time
import winsound
from gtts import gTTS
from playsound import playsound
import os
import requests
from bs4 import BeautifulSoup
import webbrowser
import pywhatkit
import pyautogui
import datetime
import random
from plyer import notification
from pygame import mixer
import pyautogui
import speedtest

winsound.Beep(1000,300)

def speak_gtts(text):
    try:
        filename = "temp_sara.mp3"
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print("gTTS error",e)


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)
#print(voices[2])
engine.setProperty("rate",170)


def speak_once(text):
    try:
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)
        engine.setProperty("rate", 170)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("TTS ERROR:",e)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

def alarm(query):
    timehere = open("alarm.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
     
'''
if __name__ == "__main__":
    while True:
        query = takeCommand()

        if query is None:
            continue
        query = query.lower()
        if "wake up sara" in query or "wake up" in query:
            from Greet_me import greetMe
            greetMe()
        

        while True:
            query = takeCommand()

            if query is None:
              continue

            query = query.lower()
            if "go to sleep" in query:
                time.sleep(0.5)
                speak("Ok sir , You can call me anytime")
                break
'''

if __name__ == "__main__":

    search_done = False

    # Wakeup loop
    while True:
        query = takeCommand()
        if query is None:
            continue
        q = query.lower().strip()
        print("DEBUG: recognized (wakeup loop):", q)
        if   "wake up sara" in q or "wake up" in q :
            from Greet_me import greetMe
            greetMe()
            
    
    # Command loop after wake
            while True:
               query = takeCommand()
               if query is None:
                 continue
               q = query.lower()

               q = q.replace("wake up sara","")
               q = q.replace("wake up","")
               q = q.replace("sara","")
               q = q.strip()
               print("DEBUG: recognized (command loop):", q)

               if  "go to sleep" in q.lower():
                    print("DEBUG: matched sleep phrase")
                    time.sleep(0.5)
                    speak_gtts("Ok sir, you can call me whenever you need")
                   # os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                    print("DEBUG: finished speaking")
                    break
               

               elif "voice call" in query or "do voice call" in query or "make voice call" in query or "call" in query.lower():
                   from Whatsapp_call import whatsapp_call_dev
                   raw = query.lower()

                   for word in {"whatsapp call","sara","voice call", "voice", "make voice call", "call", "make whatsapp call", "call on whatsapp"}:
                       raw = raw.replace(word,"")
                       name = raw.strip()
  
                   if name == "":
                       speak_gtts("please tell me contact name to call on whatsapp")
                       name = takeCommand().lower().strip()
                       time.sleep(2)

                     #  whatsapp_call_dev(name, call_type="voice")


                       if name == "" or name is "none" or name is None:
                           speak_gtts("sorry sir , i didn't get the name")
                           name = takeCommand().lower().strip()
                           continue
                
                
                   whatsapp_call_dev(name, call_type="voice")


               elif "video call" in query or "do a video call" in query or "make video call" in query or "video call" in query.lower():
                   from Whatsapp_call import whatsapp_call_dev
                   raw = query.lower()
                   raw = query.replace("video","")

                   for word in {"whatsapp video call","sara","video call", "video", "make video call", "call", "make a video call", "video call on whatsapp","video"}:
                       raw = raw.replace(word,"")
                       name = raw.strip()

                   if name == "":
                       speak_gtts("please tell me contact name to call on whatsapp")
                       name = takeCommand().lower().strip()
                       if name == "" or name is "none" or name is None:
                           speak_gtts("sorry sir , i didn't get the name")
                           name = takeCommand().lower().strip()
                           continue
                
                   whatsapp_call_dev(name, call_type="video")
               
               elif "shedule my day" in q or "schedule my day" in q or "schedule today" in q or "make my schedule" in q.lower():
                   task = [] #empty list to store tasks
                   speak_gtts("Do you want to clear old tasks sir ? yes or no")
                   #query = takeCommand()
                   query = input("whats the input sir ?: ")

                   if query and "yes" in query.lower(): # query == "yes" or query == "Yes":
                       file = open("task.txt","w")
                       file.write("")
                       file.close()
                       no_task = int(input("How many tasks do you want to add sir ? "))
                       i = 0
                       for i in range(no_task):
                           task.append(input(f"Enter task : "))
                           file = open("task.txt","a")
                           file.write(f"{i} , {task[i]}\n")
                           file.close()
                           speak_gtts("all tasks are added sir")

                   elif query and "no" in query.lower():
                       speak_gtts("How many tasks do you want to add sir ?")
                       no_task = int(input("How many tasks do you want to add sir ? "))
                       i = 0
                       for i in range(no_task):
                           task.append(input(f"Enter task : "))
                           file = open("task.txt","a")
                           file.write(f"{i} , {task[i]}\n")
                           file.close()
                           speak_gtts("all tasks are added sir")

                
               elif "what is my schedule" in q or "what's my schedule" in q or "tell me my schedule" in q or "show my schedule" in q.lower():
                   file = open("task.txt","r")
                   content = file.read()
                   file.close()
                   speak_gtts("your schedule for today is as follows sir")
                   mixer.init()
                   mixer.music.load("Sound of sara/Notification.mp3")
                   mixer.music.play()

                   notification.notify(
                       title="your schedule for today sir",
                       message = content,
                       timeout = 15
                   )

               elif "open" in query.lower():
                   query = query.replace("open","")
                   query = query.replace("sara","")
                   query = query.replace("sara open the","")
                   query = query.replace("open the ","")

                   pyautogui.press("super")
                   pyautogui.typewrite(query)
                   pyautogui.sleep(2)
                   pyautogui.press("enter")

               elif "internet speed" in query or "internet speed test" in query or "check internet speed" in query or "wifi speed" in query or "check wifi speed" in query or "check my internet spleed" in query.lower():
                   wifi = speedtest.Speedtest()
                   upload_net = wifi.upload()/1048576
                   down_net = wifi.download()/1048576
                   speak_gtts(f"sir, your internet speed is {down_net:.2f} megabits per second for downloading and {upload_net:.2f} megabits per second for uploading")
                   print(f"sir, your internet speed is {down_net:.2f} megabits per second for downloading and {upload_net:.2f} megabits per second for uploading")
            
               elif "hello" in q.lower():
                      speak_gtts("Hello sir, How are you ?")

               elif "i am fine" in q.lower():
                      speak_gtts("that's great, sir")

               elif "How are you" in q.lower():
                      speak_gtts("i'm perfect sir")

               elif "thank you" in q.lower():
                     speak_gtts("you are welcome, sir")

               elif "thanks Sara" in q or "thanks for that " in q or "thank you Sara" in q.lower():
                     speak_gtts("you are welcome, sir")

               elif "i am fine what about you" in q.lower():
                    
                    speak_gtts("i'm doing well , that's great to talk with you")

               elif "did you get it or not" in q.lower():
                   speak_gtts("yeah i ,know")

               elif "that's great" in q.lower() :
                   speak_gtts("thanks for that, Sir")

               elif "you are doing well" in q.lower():
                   speak_gtts("thnak you . what i can a do for you")

               elif "tired" in q or "Tired" in q.lower():
                   speak_gtts("Playing your favorite music to relax you, sir")
                   a = (1,2,3,4,5,6,7,8,9,10)
                   b = random.choice(a)
                   if b==1:
                       webbrowser.open("https://www.youtube.com/watch?v=jqzoEJVnYHs&list=RDMMjqzoEJVnYHs&start_radio=1")

                   elif b==2:
                       webbrowser.open("https://www.youtube.com/watch?v=9JSNBnSIXQs&list=RDMMjqzoEJVnYHs&index=2")

                   elif b==3:
                       webbrowser.open("https://www.youtube.com/watch?v=cjq1hj4stJw&list=RDMMjqzoEJVnYHs&index=5")

                   elif b==4:
                       webbrowser.open("https://www.youtube.com/watch?v=_JGGLJMpVks&list=RDMMjqzoEJVnYHs&index=11")

                   elif b==5:
                       webbrowser.open("https://www.youtube.com/watch?v=Q-qgMT1QrwQ&list=RDMMjqzoEJVnYHs&index=10")

                   elif b==6:
                       webbrowser.open("https://www.youtube.com/watch?v=6cRctjPRv6M&list=RD6cRctjPRv6M&start_radio=1")

                   elif b==7:
                       webbrowser.open("https://www.youtube.com/watch?v=BQm8RMfTEto&list=RDBQm8RMfTEto&start_radio=1")    

                   elif b==8:
                       webbrowser.open("https://www.youtube.com/watch?v=I3OPD2JLgaA&list=RDI3OPD2JLgaA&start_radio=1")     

                   elif b==9:
                       webbrowser.open("https://www.youtube.com/watch?v=DHITmcKUGik&list=RDDHITmcKUGik&start_radio=1")     

                   elif b==10:
                       webbrowser.open("https://www.youtube.com/watch?v=lBQUxEgPqUM&list=RDlBQUxEgPqUM&start_radio=1")      

               elif "open" in query or "Open" in q.lower():
                   from Dictapp import openappweb
                   openappweb(query)

               elif "news" in q or "News" in q.lower():
                   from NewsRead import latest_news
                   latest_news()

               elif "close" in q or "Close" in q.lower():
                   from Dictapp import closeappweb
                   closeappweb(q)

               elif "pause" in q or "Pause" in q.lower():
                   pyautogui.press("space")
                   speak_gtts("video paused")

               elif "play" in q or "Play" in q.lower():
                   pyautogui.press("space")
                   speak_gtts("video played")

               elif "mute" in q or "Mute" in q.lower():
                   pyautogui.press("m")
                   speak_gtts("video muted")

               elif "unmute" in q or "Unmute" in q.lower():
                   pyautogui.press("m")
                   speak_gtts("video unmuted")
                
               elif "volume up" in q or "Volume up" in q.lower():
                   from keyboard import volume_up
                   speak_gtts("increasing volume, sir")
                   volume_up()

               elif "volume down" in q or "Volume down" in q.lower():
                   from keyboard import volume_down
                   speak_gtts("decreasing volume, sir")
                   volume_down()     

               elif "next video" in q or "Next video" in q.lower():
                   pyautogui.press("shift + n")
                   speak_gtts("playing next video, sir")

               elif "cinema mode" in q or "Cinema mode" in q.lower():
                   pyautogui.press("t")
                   speak_gtts("cinema mode on , sir")

               elif "set alarm" in q or "set the alarm" in q.lower():
                   print("input time example: 10 and 10 and 10")
                   speak_gtts("Set the time sir")

                   a = input("Please tell the time := ")
                   alarm(a)
                   speak_gtts(f"Done sir, alarm is set for {a}")

               elif "full screen" in q or "ful screen" in q or "Full screen" in q.lower():
                   pyautogui.press("f")
                   if q == "full srcreen mode on":
                    speak_gtts("full screen mode on , sir")

               elif q == "full screen mode foff":
                   speak_gtts(f"full screen mode off , sir")

               elif "skip ad" in q or "Skip ad" in q.lower():
                   pyautogui.click(x=1100, y=600)
                   speak_gtts("ad skipped, sir")

               elif "remember that" in q or "sara remember that" in q or "Remember that" in q.lower():
                   rememberMsg = q.replace("remember that","")
                   rememberMsg = q.replace("sara","")
                   speak_gtts("you told me to " + rememberMsg)

                   remember = open("Remember.txt","w")
                   remember.write(rememberMsg) 
                   remember.close()

               elif "what do you remember" in q or "what you remember" in q or "What do you remember" in q.lower():
                   remember = open("Remember.txt","r")
                   speak_gtts("you told me to " + remember.read())

               elif "whatsapp" in q or "Whatsapp" in q or "What's app" in q.lower():
                   from Whatsapp import sendMessage
                   sendMessage()
                   
               elif "google" in q or "Google" in q.lower() and not search_done:
                   from Search_now import searchGoogle
                   searchGoogle(q)
                   break

               elif "youtube" in q.lower() and not search_done:
                  search_done = True
                  from Search_now import searchYouTube
                  searchYouTube(q)
                  

               elif "wikipedia" in q.lower() or "Wikipedia" in q and not search_done:
                  from Search_now import searchWikipedia
                  searchWikipedia(q)
                  break
               
               elif "calculate" in q.lower() or "Calculate" in q:
                   from Calculate_no import WolfRamAlpha
                   from Calculate_no import calc
                   q = q.replace("sara","")
                   q = q.replace("calculate","")
                   calc(q)
                   WolfRamAlpha(q)
                            
               elif "aqi" in q or "AQI" in q.lower():
                   search = "aqi in Bulandshahr"
                   #url = f"https://www.google.com/search?q={search}"
                   city = "Bulandshahr"
                   url = f"https://wttr.in/{city}?format=%a"
                   try:
                       response = requests.get(url)
                       temp = response.text.strip()

                       if temp and temp != "unknow location":
                           speak_gtts (f"The current aqi in {city} is {temp}")
                       else:
                           speak_gtts(f"Sorry, i can't fetch the Aqi right now")
                   except:
                       speak_gtts("Soory , somthing went wrong fetching the aqi")
                                  
               elif "temperature" in q or "Temperature" in q.lower():
                   search = "temaperature in Bulandshahr"
                   city = "bulandshahr"
                   url = f"https://wttr.in/{city}?format=%t"
                   #url = f"https://www.google.com/search?q={search}"
         
                   try:
                       response = requests.get(url)
                       temp = response.text.strip()

                       if temp and temp != "Unknown location":
                           speak_gtts(f"The current temperature in {city} is {temp}")
                       else:
                           speak_gtts("Sorry, i can't fetch the temperature right now")

                   except:
                       speak_gtts("Sorry, somthing went wrong while fetching the temperature")
                      
                   if temp is not None:
                       #speak_gtts("Sorry, i cann't fetch the temperature right now")
                       speak_gtts(f"current{search} is {temp}")

                   else:
                       speak_gtts(f"current{search} is {temp}")

               elif "time" in query or "Time" in query.lower():
                   strTime = datetime.datetime.now().strftime("%H:%M")
                   speak_gtts(f"Sir , the time is {strTime}")

               elif "finally sleep" in query or "Finally sleep" in q.lower():
                   speak_gtts("going to sleep , sir")
                   exit()

               elif "take picture" in query or "click picture"  in query or "take pictures" in query.lower() or "click pictures" in query.lower() :
                   from Camera_Take_picture import take_pictures_dev
                   raw = query.lower()
                   for word in {"camera","open camera","sara", "open the camera", "open that"}:
                       raw = raw.replace(word,"")
                       name = raw.strip()
                       take_pictures_dev(picture_type="image")
        
               elif "take video" in query or "click video" in query or "make video in camera" in query or "make video" in query or "start video"in query.lower() :
                   from Camera_Take_picture import take_pictures_dev
                   raw = query.lower()
                   for word in {"make video in camera","make video","sara","take video", "open video", "start video"}:
                       raw = raw.replace(word,"")
                       name = raw.strip()
                       take_pictures_dev(picture_type="video")

               elif "shutdown system" in q or "system shutdown" in q or "shutdown the system" in q or "shutdown" in q or "Shutdown" in q or "switch off the system" in q.lower():
                   speak_gtts("Are you sure sir you want to shutdown the system ? yes or no")
                   shutdown =  takeCommand()
                   time.sleep(2)
                   if shutdown == "yes" or shutdown == "do that":
                       os.system("shutdown /s /t 1")
                   elif shutdown == 'no':
                       speak_gtts("ok sir, shutdown cancelld")
                       break

               elif "restart system" in q or "system restart" in q or "restart the system" in q or "restart" in q or "Restart" in q.lower():
                   speak_gtts("Are you sure sir you want to restart the system ? yes or no")
                   shutdown =  takeCommand()
                   if shutdown == "yes":
                       os.system("shutdown /r /t 1")
                   elif shutdown == 'no':
                       speak_gtts("ok sir, restart cancelld")
                       break
                   

               elif "sleep system" in q or "system sleep" in q or "sleep the system"in q.lower():
                   speak_gtts("Are you sure sir you want to sleep the system ? yes or no")
                   shutdown =  takeCommand()
                   time.sleep(2)
                   if shutdown == "yes" or shutdown == "do that":
                       os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                   elif shutdown == 'no':
                       speak_gtts("ok sir, sleep cancelld")
                       break



