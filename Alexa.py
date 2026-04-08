import speech_recognition as sr
import pyttsx3
import datetime
import time
import wikipedia
import pywhatkit
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
mic_error_streak = 0


def talk(text):
    """Make ALexa speak the given text"""
    engine.say(str(text))
    engine.runAndWait()


def take_command():
    listener = sr.Recognizer()
    voice = None
    
    try:
        with sr.Microphone() as source:
            print('Listening.....')
            voice = listener.listen(source, timeout=5, phrase_time_limit=8)
    except sr.WaitTimeoutError:
        print('No speech detected (timeout).')
        return ''
    except (OSError, RuntimeError) as err:
        print(f'Microphone error: {err}')
        talk('I cannot access the microphone right now. Please check mic permissions and close other audio apps.')
        return None
    except Exception as err:
        print(f'Unexpected mic error: {err}')
        return None

    if voice is None:
        return ''

    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '').strip()
            print(f'Command: {command}')
            return command
        else:
            return ''
    except sr.UnknownValueError:
        print('Speech not recognized.')
        return ''
    except sr.RequestError as err:
        print(f'Speech recognition service error: {err}')
        talk('Speech service is unavailable right now. Please try again.')
        return ''
    except Exception as err:
        print(f'Unexpected speech error: {err}')
        return ''

def run_alexa():
    global mic_error_streak

    command = take_command()

    if command is None:
        mic_error_streak = min(mic_error_streak + 1, 4)
        # Exponential backoff to avoid hammering the audio stack.
        time.sleep(2 ** mic_error_streak)
        return

    mic_error_streak = 0

    if not command:
        return

    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f'Playing {song}')
        try:
            pywhatkit.playonyt(song)
        except Exception as err:
            print(f'Could not play {song}: {err}')
            talk(f'Sorry, I could not play {song}')

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(f'Current time is {current_time}')
        talk(f'Current time is {current_time}')

    elif 'who is' in command:
        person  = command.replace('who is', '').strip()
        try:
            info = wikipedia.summary(person, sentences=5)
            print(info)
            talk(info)
        except Exception:
            talk(f'Sorry, I could not find information about {person}')

    elif 'date' in command:
        talk('Sorry, I have a headache!')

    elif 'are you single' in command:
        talk('I am in a relationship with Devansh')

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'stop' in command or 'exit' in command:
        talk('Goodbye! Love')
        exit()
    
    else:
        talk('Please say the command again.')

# Greet the user on startup
talk('Hey, i am Alexa, here to assist you. Is there anything i can help you with ?')

# Keep running in a loop
while True:
    run_alexa()
    time.sleep(0.2)