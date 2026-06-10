# Functions with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Ope", "Love Island")

# Positional argument

greet_with("Love Island", "Ope")

# Keyword Arguments

greet_with(location="Love Island", name="Ope")

