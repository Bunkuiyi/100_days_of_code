import random
import hangman_words
import hangman_art

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
length_of_word = len(chosen_word)

for letter in range(length_of_word):
    placeholder += "_"
print(f"Word to guess: {placeholder}")

game_over = False
matched_letter = []
lives = 6

while not game_over:
    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in matched_letter:
        print(f"You've already guessed {guess}. ")

    display = ""

    for letter in chosen_word:
        if letter == guess :
            display += letter
            matched_letter.append(letter)
        elif letter in matched_letter:
             display += letter
        elif not letter == guess :
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life. ")
        if lives == 0:
            print(f"The correct word was {chosen_word}. You lose!")
            game_over = True

    if "_" not in display:
        game_over = True
        print("You win! ")

    print(hangman_art.stages[lives])