

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump ():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(6):
    jump()

# Do not use this code, it is only used to not get errors.
def turn_left():
    print('')
def move():
    print('')