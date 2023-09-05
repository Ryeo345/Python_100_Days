# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# when working with while loops it is important to test for edge cases to prevent infinite loops
# algorithm is to follow a path that goes along the right side
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# solution for edge case (searches for a wall for its right side)
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()



