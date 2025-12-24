# 🧠 Jarvis Voice Assistant (Python)

A fully functional **AI-powered voice assistant** built with Python — capable of performing system operations, fetching live data, responding naturally, and even **transcribing your speech into Notepad** in real time!

---

## 🚀 Features

### 🎙️ Voice Interaction
- Uses your microphone to recognize voice commands
- Natural speech responses with **pyttsx3**
- Personalized responses using your name

### 🧩 Smart Features
- **Small talk**: understands greetings like “How are you?”, “Who are you?”, “Thank you”, etc.
- **Jokes**: fetches real jokes dynamically from JokeAPI
- **Weather updates**: live temperature and condition for any city via OpenWeather API
- **News headlines**: top 10 live headlines from India via NewsAPI
- **Memory**: remembers your name and last city for next weather requests
- **Dictation mode**: after opening Notepad, you can dictate text to be typed automatically
- **Games**: Game features which includes the classic rock-paper-scissors and guess the number

### 🧠 System Commands
| Command | Action |
|----------|--------|
| `open notepad` | Opens Notepad and optionally enables dictation |
| `close notepad` | Closes Notepad |
| `open calculator` | Opens Calculator |
| `close calculator` | Closes Calculator |
| `open google` | Opens Google |
| `open chess` | Opens Chess.com in Edge |
| `weather` | Asks for city and gives current weather |
| `news` | Reads top headlines |
| `shutdown` | Shuts down Jarvis |

### 🗨️ Small Talk Examples
| You Say | Jarvis Responds |
|----------|----------------|
| “How are you?” | “All systems functional, Agent!” |
| “What’s up?” | “Monitoring the digital world, Agent.” |
| “Thank you” | “I’m a robot, Agent. No need to thank me!” |
| “Tell me a joke” | Fetches a random joke |
| “Who are you?” | “I’m Jarvis, your AI companion and helper.” |

---

## 🧰 Tech Stack

- **Python 3.8+**
- **Libraries Used:**
  - `speech_recognition` – converts speech to text
  - `pyttsx3` – converts text to speech
  - `subprocess`, `os` – for opening/closing apps
  - `requests` – fetch live weather, news, jokes
  - `webbrowser` – open websites
  - `threading` – run assistant smoothly
  - `random`, `time` – natural response & behavior

---

## ⚙️ Setup Instructions

### 1️⃣ Clone this repository
```bash
git clone https://github.com/Tuhin-adhikari/mini-jarvis.git
cd jarvis-assistant
