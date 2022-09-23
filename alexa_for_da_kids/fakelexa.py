import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say('What can I do for you?')
engine.runAndWait()

def sayit(text):
    engine.say(text)
    engine.runAndWait()

try:
    with sr.Microphone() as source:
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'spell' in command:
            print(command)
            sayit(command)
except:
    pass