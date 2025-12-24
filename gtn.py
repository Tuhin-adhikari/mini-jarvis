def gtn_game(num : int):
    """
    Play Guess the number with the user.
    """
    
    if num < 1 or num > 100:
        return "Please choose a number between 1 and 100 to play."
    
    computer_choice = randint(1, 100)
    
    if num == computer_choice:
        return f"congratulations! You guessed it right. The number was {computer_choice}."
    elif num < computer_choice:
        return f"Your guess {num} is low!. Increase the guess value"
    else:
        return f"Your guess {num} is high!. Decrease the guess value"