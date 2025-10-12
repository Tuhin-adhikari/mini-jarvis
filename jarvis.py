import speech_recognition as sr
import pyttsx3
import subprocess as sb
import webbrowser as wb
import os
import threading
import requests
import time
import random
import pyautogui  # NEW for typing automation

# Initialize TTS engine
tts_engine = pyttsx3.init()
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[1].id)  # female voice (system dependent)
tts_engine.setProperty('rate', 200)  # faster speech
tts_engine.setProperty('volume', 1.0)  # max volume

Weather_api = "e04dc12a2a81caad7be088998bd2598a"
News_api = "38ed8652716e48d8bed0ec99aa933afc"

# Memory for context
memory = {
    "user_name": None,
    "last_city": None,
    "last_command": None,
    "dictation_mode": False
}

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
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
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

# --- Command Functions ---
def open_notepad():
    speak("Opening Notepad.")
    sb.Popen(["notepad.exe"])
    time.sleep(2)  # wait for notepad to open
    speak("Do you want me to start writing what you say?")
    reply = recognize(timeout=15, phrase_time_limit=5)
    if "yes" in reply or "start" in reply:
        memory["dictation_mode"] = True
        speak("Dictation mode activated. Say 'stop writing' to exit.")

def close_notepad():
    speak("Closing Notepad.")
    os.system("taskkill /f /im notepad.exe")
    memory["dictation_mode"] = False

def dictation_loop(command):
    """Handle writing when dictation mode is ON"""
    if "stop writing" in command:
        memory["dictation_mode"] = False
        speak("Dictation mode stopped.")
    else:
        pyautogui.typewrite(command + "\n")

def open_calculator():
    speak("Opening Calculator.")
    sb.Popen(["calc.exe"])

def close_calculator():
    speak("Closing Calculator.")
    os.system("taskkill /f /im calc.exe")

def open_google():
    speak("Opening Google.")
    wb.open("https://www.google.com")

def open_chess():
    speak("Opening Chess.com.")
    sb.Popen([
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe",
        "--profile-directory=Default",
        "--app-id=kinpkbniadkppecjaginbegiljofpcfc",
        "--app-url=https://www.chess.com/",
        "--app-launch-source=4"
    ])

def open_whatsapp():
    speak("Opening WhatsApp Web.")
    wb.open("https://web.whatsapp.com")

def get_weather(city="Bangalore"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Weather_api}&units=metric"
    response = requests.get(url).json()
    
    if response.get("main"):
        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]
        speak(f"The current temperature in {city} is {temp}°C with {desc}.")
        memory["last_city"] = city
    else:
        speak("Sorry, I couldn't fetch the weather right now.")

def ask_weather():
    if memory.get("last_city"):
        speak(f"Do you want the weather for {memory['last_city']} again?")
        reply = recognize(timeout=10, phrase_time_limit=None)
        if "yes" in reply or "sure" in reply:
            get_weather(memory["last_city"])
            return
    speak("For which city do you want the weather?")
    city = recognize(timeout=10, phrase_time_limit=None)
    if city:
        get_weather(city)
    else:
        speak("I didn’t hear the city name.")

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey={News_api}"
    response = requests.get(url).json()
    
    if response.get("articles"):
        speak("Here are the top news headlines:")
        for i, article in enumerate(response["articles"][:5]):
            speak(f"{i+1}. {article['title']}")
        speak("Do you want me to read more headlines?")
        reply = recognize(timeout=5, phrase_time_limit=None)
        if "yes" in reply or "sure" in reply:
            for i, article in enumerate(response["articles"][5:10]):
                speak(f"{i+6}. {article['title']}")
        else:
            speak("Okay, moving on.")
    else:
        speak("Sorry, I couldn't fetch news right now.")

def tell_joke():
    try:
        response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single").json()
        if response.get("joke"):
            speak(response["joke"])
        else:
            speak("Hmm, I couldn't find a joke right now.")
    except:
        speak("Sorry, something went wrong while fetching a joke.")

def shutdown_assistant():
    speak(f"Shutting down. Goodbye {memory['user_name']}!")
    os._exit(0)

# --- Small Talk ---
small_talk = {
    "how are you": [f"I'm doing great, {memory['user_name']}! How about you?", "Feeling energetic, ready to assist you!", f"All systems functional, {memory['user_name']}!"],
    "what's up": ["Just keeping an eye on the system, ready to assist you.", f"Monitoring the digital world, {memory['user_name']}.", f"All quiet here, {memory['user_name']}. You?"],
    "who are you": ["I'm your personal assistant, Jarvis, at your service.", "Jarvis, your AI companion and helper."],
    "thank": [f"I'm a robot, {memory['user_name']}. No need to thank me!", f"Just doing my job, {memory['user_name']}!", "You're welcome! But technically, I don't need thanks 😎", "Thanking a robot, really?"],
    "joke": [tell_joke]
}

# --- Commands ---
commands = {
    "open notepad": open_notepad,
    "close notepad": close_notepad,
    "open calculator": open_calculator,
    "close calculator": close_calculator,
    "open google": open_google,
    "open chess": open_chess,
    "open whatsapp": open_whatsapp,
    "shutdown": shutdown_assistant,
    "shut down": shutdown_assistant,
    "weather": ask_weather,
    "news": get_news
}

# --- Personalized Greeting ---
def greet_user():
    if not memory.get("user_name"):
        speak("Hello Agent, what should I call you?")
        name = recognize(timeout=10, phrase_time_limit=None)
        if name:
            memory["user_name"] = name
            speak(f"Nice to meet you, {name}!")
        else:
            memory["user_name"] = "Agent"
            speak("No worries, I'll call you Agent.")
    else:
        speak(f"Welcome back, {memory['user_name']}!")

# --- Process Command ---
def process_command(command):
    # If in dictation mode, write instead of command
    if memory["dictation_mode"]:
        dictation_loop(command)
        return

    # Small talk
    for phrase in small_talk:
        if phrase in command:
            response = random.choice(small_talk[phrase])
            if callable(response):
                response()
            else:
                speak(response)
            return
    
    # Commands
    for key in commands:
        if key in command:
            memory["last_command"] = key
            commands[key]()  # speak is already handled inside
            return
    
    speak(f"I didn’t quite get that, {memory['user_name']}. Can you rephrase?")

# --- Main Assistant Loop ---
def assistant_loop():
    greet_user()
    print("Say 'Hello Jarvis' to activate...")
    while True:
        text = recognize()
        if "hello" in text or "jarvis" in text:
            speak(f"Yes {memory['user_name']}, how may I help you?")
            while True:
                command = recognize(timeout=15, phrase_time_limit=None)
                if command:
                    process_command(command)

# Run
if __name__ == "__main__":
    assistant_loop()
