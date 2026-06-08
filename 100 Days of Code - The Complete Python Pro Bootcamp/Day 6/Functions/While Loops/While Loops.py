# while something_is_true:
    #Do this
    #Then do this
    #Then do this
# Continue to do it till condition is false

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle() :
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# for race in range(1, 7):
#    hurdle()


# Reeborg's world Hurdle 2
while not at_goal():
    hurdle()

# Reeborgs world Hurdle 3
while not at_goal():
    if wall_in_front():
        hurdle()
    elif front_is_clear():
        move()

# Reeborg's world Hurdle 4
def hurdle() :
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        hurdle()
    elif front_is_clear():
        move()

# Reeborg's world Maze
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear() :
        move()
    else:
        turn_left()
