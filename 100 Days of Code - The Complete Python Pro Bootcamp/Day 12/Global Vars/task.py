# Modifying Global Scope

enemies = 1


# def increase_enemies():
#     global enemies # Avoid modifying global scope within a function that has local scope
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

def increase_enemies(enemy):
    return enemy + 1
    print(f"enemies inside function: {enemies}")


enemies = increase_enemies(enemies) # this function does the same as the function above without modifying global scope using return

increase_enemies()
print(f"enemies outside function: {enemies}")


