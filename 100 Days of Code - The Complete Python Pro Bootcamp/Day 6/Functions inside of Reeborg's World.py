# Reeborg's world hurdle 1

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

for race in range(1, 7):
    hurdle()