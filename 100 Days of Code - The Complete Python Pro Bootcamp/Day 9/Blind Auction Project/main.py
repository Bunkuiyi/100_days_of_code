import art
print(art.logo)

# print("\n" * 100)

# TODO-1: Ask the user for input

# name = input("What is your name?: ")
# bid = int(input("What is your bid?: "))

# TODO-2: Save data into dictionary {name: price}

# name_bid = {}
# name_bid[name] = bid
#
# print(name_bid)

# TODO-3: Whether if new bids need to be added

auction_over = True
name_bid = {}

while auction_over:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: £"))
    answer = input("Are there any more bids. Type yes if there are. Othwerwise type no. ").lower()

    name_bid[name] = bid

    if answer == "yes":
        print("\n" * 100)
    elif answer == "no" :
        auction_over = False
    else:
        print("That was in incorrect input. Try again! ")

highest_bid = 0
name_highest_bid = ""

for name in name_bid:
    bid = name_bid[name]
    if bid > highest_bid :
        highest_bid = bid
        name_highest_bid = name

print(f"Congratulations! {name_highest_bid} had the highest bid at {highest_bid}. ")

# TODO-4: Compare bids in dictionary

# highest_bid = 0
# name_highest_bid = ""
#
# for name in name_bid:
#     bid = name_bid[name]
#     if bid > highest_bid :
#         highest_bid = bid
#         name_highest_bid = name
#
# print(f"Congratulations! {name_highest_bid} had the highest bid at {highest_bid}. ")