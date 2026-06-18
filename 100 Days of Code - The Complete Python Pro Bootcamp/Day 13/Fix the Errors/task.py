try:
    age = int(input("How old are you? "))
except ValueError:
    print("That was an incorrect input! Try again with numbers like '15'. ")
    age = int(input("How old are you? "))

if age > 18:
    print(f"You can drive at age {age}. ")
