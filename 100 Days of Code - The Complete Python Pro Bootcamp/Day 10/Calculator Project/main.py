import art


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

calculator_functions = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


# while continue_solving:
#     if start_finish == "y":
#         n1 = answer
#     elif start_finish == "n":
#         continue_solving = False
#         continue
#     else:
#         n1 = int(input("Type in the first number:\n"))
#     operator = input("Pick a mathematical operator: +, -, * or /.\n")
#     n2 = int(input("Type in the second number.\n"))
#
#     if operator == "+":
#             answer = calculator_functions["+"](n1, n2)
#             print(f"{n1} + {n2} = {answer}")
#     elif operator == "-":
#             answer = calculator_functions["-"](n1, n2)
#             print(f"{n1} - {n2} = {answer}")
#     elif operator == "*":
#             answer = calculator_functions["*"](n1, n2)
#             print(f"{n1} * {n2} = {answer}")
#     elif operator == "/":
#             answer = calculator_functions["/"](n1,n2)
#             print(f"{n1} / {n2} = {answer}")
#     else:
#             print("That was an incorrect input. Try again!")
#
#     start_finish = input(f"Type y to continue solving with {answer}, or type n to start a new calculation: ")
def calculator():
    print(art.logo)
    continue_solving = True
    numb1 = float(input("Type in your first number: "))

    while continue_solving:
        for symbol in calculator_functions:
            print(symbol)
        calculator_symbols = input("Pick an operation: ")
        numb2 = float(input("Type in your second number: "))
        answer = calculator_functions[calculator_symbols](numb1, numb2)
        print(f"{numb1} {calculator_symbols} {numb2} = {answer}")

        start_finish = input(f"Type 'y' to continue solving with {answer}, or type 'n' to start a new calculation: ")

        if start_finish == "y":
                numb1 = answer
        else:
            continue_solving = False
            print("\n" * 20)
            calculator()

calculator()

