MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def format_resources():
    """Takes the resources left in the coffee machine and returns the printable format"""
    water_resources = resources["water"]
    milk_resources = resources["milk"]
    coffee_resources = resources["coffee"]
    money_resources = resources["money"]
    print(f"Water: {water_resources}ml\nMilk: {milk_resources}ml\nCoffee: {coffee_resources}g\nMoney: £{money_resources}")

# check if resources are sufficient
def check_resources(user_drink):
    """Take a user's drink and the resources needed and returns if there are enough to make the drink"""
    ingredients = MENU[user_drink]["ingredients"]
    for item in ("water", "milk", "coffee"):
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# process coins
def process_coins():
    """Prompts user for coins and returns total value inserted."""
    print("Please insert coins.")
    one_penny = int(input("How many 1p coins?: "))
    two_pennies = int(input("How many 2p coins?: "))
    five_pennies  = int(input("How many 5p coins?: "))
    ten_pennies  = int(input("How many 10p coins?: "))
    twenty_pennies = int(input("How many 20p coins?: "))
    fifty_pennies = int(input("How many 50p coins?: "))
    one_pound = int(input("How many £1 coins?: "))
    two_pounds = int(input("How many £2 coins?: "))
    return one_penny * 0.01 + two_pennies * 0.02 + five_pennies * 0.05 + ten_pennies * 0.10 + twenty_pennies * 0.20 + fifty_pennies * 0.50 + one_pound * 1.0 + two_pounds * 2.0

# make coffee and deduct resources
def make_coffee(drink):
    """Deducts ingredients and serves the drink."""
    ingredients = MENU[drink]["ingredients"]
    for item in ("water", "milk", "coffee"):
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. Enjoy!")

# check if transaction is successful
def check_transaction(inserted, drink):
    """Returns True and handles change/profit if enough money was inserted."""
    cost = MENU[drink]["cost"]
    if inserted < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    change = round(inserted - cost, 2)
    if change > 0:
        print(f"Here is £{change:.2f} pounds in change.")
    resources["money"] = round(resources["money"] + cost, 2)
    return True

def main():
    switch_off = False
    while not switch_off:
        drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if drink_choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            switch_off = True
        # print report
        elif drink_choice == "report":
            format_resources()

        elif drink_choice in MENU:
            if check_resources(drink_choice):
                inserted = process_coins()
                if check_transaction(inserted, drink_choice):
                    make_coffee(drink_choice)

        else:
            print(f"'{drink_choice}' is not a valid option. Please choose espresso, latte, or cappuccino.")

main()