import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Initial code

# rps_game = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
# list_rps = [rock, paper, scissors]
#
# if rps_game == "0" :
#     print(rock)
# elif rps_game == "1" :
#     print(paper)
# elif rps_game == "2":
#     print(scissors)
# else:
#     print("That was the wrong input. Try Again!")
#
# print("Computer chose:")
#
# win_loss = random.choice(list_rps)
#
# print(win_loss)
#
# if rps_game == "0" and win_loss == list_rps[0] :
#     print("It's a draw")
# elif rps_game == "0" and win_loss == list_rps[2] :
#     print("You win")
# elif rps_game == "0" and win_loss == list_rps[1] :
#     print("You lose")
# elif rps_game == "1" and win_loss == list_rps[1] :
#     print("It's a draw")
# elif rps_game == "1" and win_loss == list_rps[0] :
#     print("You win")
# elif rps_game == "1" and win_loss == list_rps[2] :
#     print("You lose")
# elif rps_game == "2" and win_loss == list_rps[0] :
#     print("You lose")
# elif rps_game == "2" and win_loss == list_rps[1] :
#     print("You win")
# elif rps_game == "2" and win_loss == list_rps[2] :
#     print("It's a draw")

# Simplified

choices = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if player not in [0, 1, 2]:
    print("That was the wrong input. Try Again!")
else:
    print(choices[player])

    computer = random.randint(0, 2)
    print("Computer chose:")
    print(choices[computer])

    if player == computer:
        print("It's a draw")
    elif (player - computer) % 3 == 1:
        print("You win")
    else:
        print("You lose")







