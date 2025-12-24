from random import randint

def rps_game(text : str):
    """
    Play Rock, Paper, Scissors with the user.
    """
    
    choices = ["rock", "paper", "scissors"]
    if text not in choices:
        return "Please choose rock, paper, or scissors to play."
    
    user_choice = text
    computer_choice = choices[randint(0, 2)]
    
    if user_choice == computer_choice:
        return f"Both chose {user_choice}. Hence, it is a tie!"
    elif (user_choice == "rock"):
        if computer_choice == "scissors":
            return f"My choice was {computer_choice}. Rock crushes Scissors! You win!"
        else:
            return f"My choice was {computer_choice}. Paper covers Rock! I wins!"
    elif (user_choice == "paper"):
        if computer_choice == "rock":
            return f"My choice was {computer_choice}. Paper covers Rock! You win!"
        else:
            return f"My choice was {computer_choice}. Scissors cut Paper! I wins!"
    elif (user_choice == "scissors"):
        if computer_choice == "paper":
            return f"My choice was {computer_choice}. Scissors cut Paper! You win!"
        else:
            return f"My choice was {computer_choice}. Rock crushes Scissors! I wins!"
        
    return "Error in game logic. Please try again."