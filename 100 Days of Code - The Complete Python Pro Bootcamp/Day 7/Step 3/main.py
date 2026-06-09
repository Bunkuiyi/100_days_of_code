# TODO-1
# - Use a while loop to let the user guess again.
# - The loop should only stop once the user has guessed all the letters in the chosen_word.
# - At that point `display` has no more blanks ("_"). Then you can tell the user they've won.

game_over = False

while not game_over:
    # Step 1 and 2 code in here

    if not "_" in display:
        game_over = True
        print("You win! ")

# TODO-2
# - Update the for loop so that previous guesses are added to the `display` String.
# - At the moment, when the user makes a new guess, the previous guess gets replaced by a "_". We need to fix that by updating the for loop.
    matched_letters = []

    elif letter not in matched_letters:
        letter += display