import random
import art

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(user_guess, actual_answer, turns):
    """Check users' guess against actual number, returns number of turns left"""
    if user_guess > actual_answer:
        print("Too high. ")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low. ")
        return  turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

def set_difficulty():
    """Sets difficulty returns depending on easy or hard level selected"""
    level = input("Choose a difficulty. Type 'easy' or 'hard'. ").lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    """Plays the guess the number guess"""
    print(art.logo)
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100) # Choosing a random number between 1 and 100

    turns = set_difficulty()


    # Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts to guess the number. ")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You're out of guesses. You lose.")
            return

game()


