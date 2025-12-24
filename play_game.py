import speech_recognition as sr
import pyttsx3
from jarvis import recognize

tts_engine = pyttsx3.init()
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[1].id)  #Female Voices
tts_engine.setProperty('rate', 200)  # Faster Speech
tts_engine.setProperty('volume', 1.0)  # Max Volume



def game():
    """
    Playing games with the computer.
    """
    
    game_choices = ["rock_paper_scissors", "guess_the_number"]
    
    speak("Which game would you like to play? You can choose Rock Paper Scissors or Guess the Number.")
    user_choice = recognize(timeout=5, phrase_time_limit=5)
    if "rock" in user_choice or "paper" in user_choice or "scissors" in user_choice:
        from rps import rps_game
        speak("Great! Let's play Rock Paper Scissors. Please say your choice.")
        user_move = recognize(timeout=5, phrase_time_limit=3)
        result = rps_game(user_move)
        speak(result)
    elif "guess" in user_choice or "number" in user_choice:
        from gtn import gtn_game
        speak("Awesome! Let's play Guess the Number. Please guess a number between 1 and 100.")
        computer_number = random.randint(1, 100)
        count_guess = 0
        while True:
            speak("Enter you're number in the console.")
            user_number_text = input("Your guess: ")
            try:
                user_number = int(user_number_text)
                result = gtn_game(computer_number, user_number)
                speak(result)
                if "congratulations" in result:
                    speak(f"You guessed the number in {count_guess + 1} attempts. Well done!")
                    break
                count_guess += 1
            except ValueError:
                speak("That doesn't seem to be a valid number. Please try again.")
    else:
        speak("I didn't catch that. Please choose either Rock Paper Scissors or Guess the Number to play.")