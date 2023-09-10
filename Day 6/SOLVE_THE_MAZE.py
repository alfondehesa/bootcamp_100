
# Do not use this code, it is only used to not get errors.
def turn_left():
    pass
def move():
    pass
def at_goal():
    pass
def front_is_clear():
    pass
def wall_on_right():
    pass
def wall_on_left():
    pass

# Only use this code.
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()


while not at_goal():
    while (not wall_on_right()) and (not at_goal()) :
        turn_right()
        move()
    while wall_on_right() and front_is_clear() and (not at_goal()):
        move()
    while (not front_is_clear()) and (not at_goal()):
        if (not wall_on_right()) and (not at_goal()):
            turn_right()
            move()
        else:
            turn_left()

