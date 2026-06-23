import game_data
import art
import random

def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

SCORE = 0
# Display art
print(art.logo)
game_over = False
account_b = random.choice(game_data.data)

while not game_over:
# Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(game_data.data)
    if account_a == account_b:
        account_b =  random.choice(game_data.data)

    print(f"Compare A: {format_data(account_a)} ")
    print(art.vs)
    print(f"Against B: {format_data(account_b)} ")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n"* 20)
    print(art.logo)

    # CHECK IF USER IS CORRECT
    ## Get follower count of each account
    followercount_a = account_a["follower_count"]
    followercount_b = account_b["follower_count"]

    is_correct = check_answer(guess, followercount_a, followercount_b)

    # Give user feedback on their guess
    if is_correct:
        SCORE += 1
        print(f"You got it right, well done! Current score: {SCORE} ")
    else:
        print(f"You were wrong, unlucky! Final score: {SCORE} ")
        game_over = True

## Making account at position B become next account at position A