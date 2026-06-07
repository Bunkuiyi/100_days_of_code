# fruits = ["Apple", "Peach", "Pear"]
#
# # loop executes same line of code multiple times
#
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

import random

numbers = [random.randint(0, 100)]

for number in numbers:
    print(number)
    if 0 <= number <= 50:
        print("This is a test. ")