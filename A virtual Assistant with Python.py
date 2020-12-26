A virtual Assistant with Python

Install packages
# pip install pyttsx3
# pip install speechrecognition
# pip install webbrowser
# pip wikipedia

Import libraries
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import setuptools

Speak Function
def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()
def Hello():
    speak('''Hi there! I am your virtual assistant, how may I help you''')

Voice Recognizer
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print("The command is printed=", Query)
        except Exception as e:
            print(e)
            print("Please repeat that")
            return "None"
        return Query

Query Receiver
def Take_query():
    Hello()
    while(True):
        query = takeCommand().lover()
        if "hello how are you" in query:
            speak("I am fine")
        elif "open google" in query:
            speak("Open Google")
            webbrowser.open("www.google.com")
        # the program stops here        
        elif "bye" in query:
            speak("Okay see you next time")
            exit()
        elif "from wikipedia" in query:
            speak("Checking wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(result)
        elif "tell me your name" in query:
            speak("I am Kay. Your assistant")

Call Assistant
if __name__ == '__main__':
    # main method to execute the function
    Take_query()


