from turtledemo.nim import computerzug

import art
import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Returns the sum of cards in hand as the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0 # 0 is Blackjack
    if 11 in cards and sum(cards) > 21:
        cards[0] = 1
    return sum(cards)

def compare (u_score, c_score):
    """Compare's the user hand against the computers hand to see who wins"""
    if c_score == u_score:
        return "It's a draw!"
    elif c_score == 0:
        return "The computer got Blackjack! You lose."
    elif u_score == 0:
        return "You got Blackjack! You win."
    elif u_score > 21:
        return "You lose!"
    elif c_score > 21:
        return "You win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"

def blackjack():
    print (art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            draw_again = input("Would you like to draw another card. Type 'y' for yes and 'n' for no. ").lower()
            if draw_again == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score <= 16 :
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, your final score: {user_score} ")
    print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_score} ")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack> Type 'y' or 'n'. ").lower():
    print("\n" * 20)
    blackjack()

