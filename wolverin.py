import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Sir!!")
    elif hour>=12 and hour<=18:
        speak("good evening sir!!")
    else:
        speak("Good Evening sir!!")
    speak("i am Wolverine sir!!, please tell mehh hoew may i help youu!!")    

def takecommand():
    # it will takes microphoone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source, timeout=3)
    try:
        print("Recognizing......")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        print("say it again!.")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail.com','your password')
    server.sendmail('youremail.com',to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    # while True:
    if 1:
        query=takecommand().lower()

        # logic for axecuting tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query, sentences=2)
            speak('acording to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        # elif 'play music' in query:
            # music_dir=

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif 'open code' in query:
            codePath="C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to sam' in query:
            try:
                speak("what shoul i say")
                content=takeCommand()
                to="sam12@gmail.com"
                sendEmail(to,content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak("sorry!i'm not able to send this email")