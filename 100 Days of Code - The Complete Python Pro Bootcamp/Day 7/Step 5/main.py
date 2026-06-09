# TODO-1:
# - Update the word list to use the `word_list` from hangman_words.py

import hangman_words.py
from hangman_words import word_list

# TODO-2:
# - Update the code to use the `stages` from the file hangman_art.py

import hangman_art.py
from hangman_art import stages, logo

# TODO-3:
# - Import the `logo` from hangman_art.py and print it at the start of the game.

print(hangman_art.logo)
from hangman_art import logo

# TODO-4:
# - If the user has entered a letter they've already guessed, print the letter and let them know.
# - We should not deduct a life for this.
# - e.g. You've already guessed a

if guess in matched_letter:
    print(f"You've already guessed {guess}. ")

# TODO-5:
# - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
# - e.g. You guessed d, that's not in the word. You lose a life.

print(f"You guessed {guess}, that's not in the word. You lose a life. ")

# TODO-6:
# - Update the code below to tell the user how many lives they have left.

print(f"****************************<???>/{lives} LIVES LEFT****************************")

# TODO 7:
# - Update the print statement to give the user the correct word they were trying to guess.
# - e.g. `IT WAS <Correct Word>! YOU LOSE`

print(f"The correct word was {chosen_word}. You lose! ")