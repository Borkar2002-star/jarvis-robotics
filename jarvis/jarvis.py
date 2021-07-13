import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am vishakha. please tell me how may i help you")

def takeCommand():
    # it takes microphone input from the user and return string as output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        # seconds of non-speaking audio before a phrase is considered complete
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query

def sendEmail(do,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('vishakhaborkar79@gmail.com','Vishu@123')
    server.sendmail('vishakhaborkar79@gmail.com',to,content)
    server.close()

if __name__== "__main__":
    # speak("Vishakha is a good girl")
    # wishMe()
    # takeCommand() 
    while True:
    # if 1:
        query=takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
             webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
             webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
             webbrowser.open("facebook.com")

         elif 'open instagram' in query:
             webbrowser.open("instagram.com")

        elif 'play music' in query:
            music_dir='C:\\Users\\VISHAKHA\\Downloads\\songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"mam, the time is {strTime}")

        elif 'open code' in query:
            codePath="C:\\Users\\VISHAKHA\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)

        elif 'email to vishakha' in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to="vishakhaborkar79@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend vishakha. i am not able to send email")
