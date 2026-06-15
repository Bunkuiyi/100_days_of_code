enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope - exists within functions

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()

# Global Scope (only difference is where you define function) - available anywhere as it is not within another function

play_health = 10

def drink_potion():
    potion_strength = 2
    print(play_health)

drink_potion()