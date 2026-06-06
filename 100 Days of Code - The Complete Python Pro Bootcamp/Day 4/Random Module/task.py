import random # module is python file
# import my_module # my_module if the file
#
# random_integer = random.randint(1, 10)  # randint is variable from random module
# print(random_integer)
#
# print(my_module.my_favourite_number)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

print("Welcome to the coinflip game, for helping you make tough decisions")
coin = input("Choose Heads or Tails! ")
decision = random.randint(1,2)

if coin == "Heads" and decision == 1 :
    print("You landed on Heads! You won! ")
elif coin == "Heads" and decision == 2 :
    print("You landed on Tails! You lost! ")
elif coin == "Tails" and decision == 1 :
    print("You landed on Heads! You lost! ")
elif coin == "Tails" and decision == 2 :
    print ("You landed on Tails! You won!")
else :
    print("That was the wrong input. Try again! ")

