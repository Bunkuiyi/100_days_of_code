print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
ticket = 0
# elif (else if) used in conditional statements to check for multiple conditions e.g. if first condition is false, it moves onto next 'elif' statement to check if the condition is true

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age "))
    if age <= 12:
        print("Your ticket will cost £5 per person.")
        ticket = 5
    elif age <= 18:
        print("Your ticket will cost £7 per person.")
        ticket = 7
    else :
        print ("Your ticket will cost £12 per person.")
        ticket = 12
    group = input("Are you in a group of more than 4? Please answer with Yes or No. ")
    number_in_group = int(input("How many people are in your group? "))
    if group == ("Yes") :
        final = ticket * number_in_group
        final -= 5
        print(f"We can offer you £5 off!\nYour new price is £{final}")
    else :
        print("Sorry, we can't offer you in any deals today")
else:
    print("Sorry you have to grow taller before you can ride.")
