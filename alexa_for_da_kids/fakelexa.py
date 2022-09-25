import speech_recognition as sr
import pyttsx3
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def spellit(text):
    talk(text)
    for a in text:
        talk(a)
    talk(text)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'how do you spell' in command:
        command = command.replace('how do you spell', '')
        print(command)
        spellit(command)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

while True:
    run_alexa()
