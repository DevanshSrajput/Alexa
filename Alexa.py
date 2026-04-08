import speech_recoginition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import pyjokes

def talk(text):
    """Make ALexa speak the given text"""
    engine=pyttsx3.init() #Reinitialize engine everytime
    voices = engine.getProperty('voices')
    engine.setProperty('voice'. voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine .stop() #Stop the engine after speak


def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('Listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(f'Command: {command}')
                return command