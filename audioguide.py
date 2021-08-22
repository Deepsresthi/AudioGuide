import pyttsx3  # text to speech
import datetime  # to give date and time
import wikipedia  # to open wiki
import webbrowser  # to display web app
import os  # interacts with OS
import numpy as np  # to deal with arrays
import time  # to get live time
from selenium import webdriver  # for testing web app
import speech_recognition as sr  # speech to text


# pyppsx3 supports two voices(M&F) provided by sapi5
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # 0-male 1-female
engine.setProperty('voice', voices[0].id)


def google_search():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak('What do you want to search about')
        r.pause_threshold = 1
        audio = r.listen(source)
        topic = r.recognize_google(audio)

    search_string = topic.replace(' ', '+')
    browser = webdriver.Chrome('chromedriver')

    for i in range(1):
            matched_elements = browser.get("https://www.google.com/search?q=" +
                                      search_string + "&start=" + str(i))


def youtube_search():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak('What do you want to search about')
        r.pause_threshold = 1
        audio = r.listen(source)
        topic = r.recognize_google(audio)

    search_string = topic.replace(' ', '+')
    browser = webdriver.Chrome('chromedriver')

    for i in range(1):
            matched_elements = browser.get("https://www.youtube.com/search?q=" +
                                      search_string + "&start=" + str(i))


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("I am CURIN. Please tell me how may I help you!")


def meetup():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak('hello everyone i am CURIN')
        speak('i am a personal assistant made using PYTHON')
        speak('i use google speech recognition to listen voices and python library to answer you back')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        task = r.recognize_google(audio, language='en-in')

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return task


if __name__ == "__main__":
    wishMe()  # to greet the user
    while True:

        query = takeCommand().lower()  # to convert the command into lower case

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google me something' in query:
            google_search()

        elif 'can you search me something on youtube' in query:
            youtube_search()

        elif 'introduce yourself to everyone' in query:
            meetup()

        elif 'go to sleep' in query:
            speak('Have a good day boss')
            break
        elif 'who is my doctor' in query:
            speak('please check room 101 with medical records')
            break
        elif 'what are the risks of surgery' in query:
            speak(
                'with any surgery you face general risks like- anesthesia,infection,or bleeding.')
            break
        elif 'where is the COVID vaccination drive' in query:
            speak('please go to second floor, room 202')
            break
        elif 'when will i be able see my doctor' in query:
            speak('Patients who have a higher acuity of illness may be treated before those patients with less severe conditions. To know your timings please approach the ER nurse. Your patience is always appreciated.')
            break
        elif 'where is the emergancy ward' in query:
            speak('room 100 ground floor')
            break
        elif 'when are the visiting hours' in query:
            speak('6pm to 9pm')
            break
        elif 'where do i go to donate blood' in query:
            speak('room 103 located on first floor')
            break
        elif 'how do i get my discharge summary' in query:
            speak('it will be given by nursing staff at the time of discharge')
            break
        elif 'what is the system of billing' in query:
            speak('billing is done on a 24 hour basis')
            break
        elif 'do u have an ambulance service' in query:
            speak('yes we have an ambulance service round the clock')
            break
        elif 'where is the medical store' in query:
            speak('ground floor')
            break
        elif 'where can i meet a pediatrician' in query:
            speak('fourth floor room 401')
            break
        elif 'where can i get my COVID test' in query:
            speak('first floor room 100')
            break
        elif 'where is the general ward' in query:
            speak('second floor room 203')
            break
        elif 'where is the washroom' in query:
            speak('ground floor on the right')
            break

        elif 'Is the doctor free at this moment' in query:
            speak('NO, please make an appointment through our app ')
            break

        elif 'where is the X-ray room' in query:
            speak('Its on the third floor towards the right')
            break

        elif 'Is it compulsory to make an appointment or can i just walk in' in query:
            speak('Yes it is compulsory to make an appointment')
            break

        elif 'Where is the medical shop' in query:
            speak('There is one on the ground floor next to the reception and there is one right outside our hospital')
            break

        elif 'Which way toward the emergency' in query:
            speak('the third door on the ground floor')
            break

        elif 'Is the dermotoligist available at the moment' in query:
            speak('The doctor will be availble between 10 a.m and 4 p.m')
            break

        elif 'When can i consult the pediatrician' in query:
            speak('Doctor will be available between 9 a.m and 3 p.m ')
            break

        elif 'what time are the visiting hours' in query:
            speak('Visiting hours are from 4 p.m to 6 p.m')
            break

        elif 'where is the operation theatre' in query:
            speak('it is on the third floor on the left. Room 241')
            break

        elif 'Does this hospital have a blood bank' in query:
            speak('Yes it does please contact the front desk for further information')
            break

        elif 'Where is the cafeteria' in query:
            speak('Its on the fourth floor')
            break

        elif 'Does this hospital have a cardioligist' in query:
            speak('yes it does.')
            break

        elif 'what are the consultation hours of the ENT specialist' in query:
            speak('Doctor will be available from 5 p.m to 8 p.m')
            break

        elif 'what are the visiting hours' in query:
            speak('Visiting hours are between 4 p.m to 6 p.m')
            break

        elif 'What are the covid vaccinations available' in query:
            speak('covishield and covin')
            break

        elif 'does this hospital conduct covid tests' in query:
            speak('Yes . please head to room 120 on the first floor')
            break

        elif 'What are the OPD timings' in query:
            speak('9 a.m to 1 p.m')
            break

         elif 'Is cosmetic surgery done here' in query:
            speak('Yes it is. ')
            break
        
         elif 'Are there physiotheraphy facilities available' in query:
            speak('yes please contact the orthopedic department')
            break
        
        


