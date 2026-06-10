# You are going to write a function called calculate_love_score() that tests the compatibility between two names.
# To work out the love score between two people:
#
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
# 2. Then check for the number of times the letters in the word LOVE occurs.
#
# 3. Then combine these numbers to make a 2 digit number and print it out.

def calculate_love_score(name1, name2):
    total_true = 0
    total_love = 0
    for letter in name1 + name2:
        if letter.lower() in "true":
            total_true += 1
        if letter.lower() in "love":
            total_love += 1
    total = (str(total_true) + str(total_love))
    print(total)


calculate_love_score("Kanye West", "Kim Kardashian")