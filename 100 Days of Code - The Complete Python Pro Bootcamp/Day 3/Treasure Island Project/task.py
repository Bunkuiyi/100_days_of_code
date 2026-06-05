print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You're at a cross road. Where do you want to go?\n Type left or right. ")

if direction == "left" :
    lake = input("You've come to a lake. There is an island in the middle of the lake.\n   Type wait to wait for a boat. Type swim to swim across. ").lower()
    if lake == "wait" :
        door = input("You arrive at the island unharmed. There is a house with 3 doors.\n   One red, one yellow and one blue. Which colour do you choose. ").lower()
    else:
        print("You can't swim and therefore you drowned. Game Over.")

    if door == "yellow" :
        print("You walk into a room with a treasure chest laden with gold in the centre of it. \nYou Win!")
    elif door == "red" :
        print("You walk into a room with burning hot lava in, you fall in and get burnt to ashes. \nGame Over. ")
    elif door == "blue" :
        print("You walk into a room that is at absolute zero and you get frozen instantly. \nGame Over. ")
    else :
        print("That was an incorrect input. Try again to claim your treasure! ")

else :
    print("You've come to a forest and been attacked by a bear. Game Over.")