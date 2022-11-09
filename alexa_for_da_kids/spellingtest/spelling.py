import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

num_words = 12
words = []

for i in range(1, num_words + 1):
    words.append(input(f"Enter word #{i}: "))

lol = '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n'
print(lol * 25)

def say_word():
    index = input("Which word would you like to hear? #: ")
    try:
        index = int(index) - 1
        pyttsx3.speak(words[index])
    except ValueError:
        print("Try again!")

while True:
    say_word()
