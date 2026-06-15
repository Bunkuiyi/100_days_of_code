# There is no Block Scope in Python!
game_level = 10
enemies = ["Skeletons", "Zombies", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()