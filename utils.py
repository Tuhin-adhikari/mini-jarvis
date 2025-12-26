import speech_recognition as sr
import pyttsx3

# Initialize TTS engine
tts_engine = pyttsx3.init()
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[1].id)
tts_engine.setProperty('rate', 200)
tts_engine.setProperty('volume', 1.0)

def speak(text):
    print("Jarvis:", text)
    tts_engine.say(text)
    tts_engine.runAndWait()

# Recognizer
recognizer = sr.Recognizer()

def recognize(timeout=10, phrase_time_limit=None):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        try:
            audio = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit
            )
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that.")
            return ""
        except sr.RequestError:
            speak("Could not request results from Google.")
            return ""
