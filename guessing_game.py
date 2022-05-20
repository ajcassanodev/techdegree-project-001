"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
game_scores = []
games_won = 0

def start_game():
    """Psuedo-code Hints
    
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    times_guess = 0
    guess = 3
    print("Welcome to the number guessing game!!!")
    player_name = input("Please enter your name > ")
    print("Welcome {}! ".format(player_name))
    ran_num = random.randrange(1,10)
    print(ran_num)
    while True:
        if guess == 0:
            print("You lost! please try again ! ")
            game_scores.append(50)
            break
        play_guess = int(input("Please select a number between 1 and 10 >"))
        try:
            play_guess = int(input("Please select a number between 1 and 10 >"))
            if play_guess <= 1:
                raise ValueError ("Sorry please select a number 1-10 ")
        except ValueError as err:
            print("{}".format(err))
        if play_guess < ran_num:
            times_guess += 1
            guess -= 1
            print("That is not the right number, try higher")
            print("You now have {} guesses left!".format(guess))
            continue
        elif play_guess > ran_num:
            times_guess += 1
            guess -= 1
            print("That is not the right number, try lower")
            print("You now have {} guesses left!".format(guess))
            continue
        elif play_guess == ran_num:
            times_guess += 1
            game_scores.append(times_guess)
            print("you guessed right !!! it took you {} tries.".format(times_guess))
            print("The game is over ! please try again later ! Thanks for playing {}".format(player_name))
            break
# Kick off the program by calling the start_game function.
start_game()

while True:
    new_game = input("Would you like to play a new game? (yes/no)")
    if new_game == 'yes':
        print("the current score to beat is: {} ".format(min(game_scores)))
        start_game()
        continue
    elif new_game == 'no':
        print("No problem have a great day")
        break    