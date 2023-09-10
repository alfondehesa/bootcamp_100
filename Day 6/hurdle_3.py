
# Do not use this code, it is only used to not get errors.
def turn_left():
    pass
def move():
    pass
def at_goal():
    pass
def front_is_clear():
    pass

# Only use this code.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump ():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not(at_goal()):
    
    while front_is_clear():
        move()
    
    jump()
