def gtn_game(computer_choice: int, user_choice : int):
    """
    Play Guess the number with the user.
    """
    
    if user_choice < 1 or user_choice > 100:
        return "Please choose a number between 1 and 100 to play."
        
    if user_choice == computer_choice:
        return f"congratulations! You guessed it right. The number was {computer_choice}."
    elif user_choice < computer_choice:
        return f"Your guess {user_choice} is low!. Increase the guess value"
    else:
        return f"Your guess {user_choice} is high!. Decrease the guess value"