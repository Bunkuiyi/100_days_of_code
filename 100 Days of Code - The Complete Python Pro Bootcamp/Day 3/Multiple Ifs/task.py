print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are £5. ")
    elif age <= 18:
        print("Youth Tickets are £7.")
        bill = 7
    else:
        print("Adult tickets are £12.")
        bill = 12

    photo = input("Do you want to purchase a photo. Type y for Yes and n for No. ")
    if photo == "y" :
        # Add £ to their bill
        bill += 3

    print(f"Your final bill is £{bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
