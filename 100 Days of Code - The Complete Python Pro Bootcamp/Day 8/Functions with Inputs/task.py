def greet() :
    email = input("What's your email provider? ")
    print(f"Check your {email}. ")
    print("For the update. ")
    print("Put the cake mix. ")

greet()

# Functions that allow for inputs

def greet_with_name(name):
    print(f"Hello {name}. ")
    print(f"How do you do {name}. ")

greet_with_name("Ope")

# 'name' inside the function = 'Ope' data given that replace 'name' inside the function
# 'name' is the parameter (name of the data)
# 'Ope' is the argument (actual value of data)