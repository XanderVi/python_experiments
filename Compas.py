
# light_x: the X position of the camp_fire
# light_y: the Y position of the camp_fire
# initial_tx: Your's starting X position
# initial_ty: Your's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# travel loop
while True:
    
    direction = ""
    if initial_tx > light_x and initial_ty > light_y:
        direction = "NW"
        initial_tx -= 1
        initial_ty -= 1
    elif initial_tx > light_x and initial_ty == light_y:
        direction = "W"
        initial_tx -= 1
        initial_ty -= 0
    elif initial_tx > light_x and initial_ty < light_y:
        direction = "SW"
        initial_tx -= 1
        initial_ty += 1
    elif initial_tx == light_x and initial_ty < light_y:
        direction = "S"
        initial_tx += 0
        initial_ty += 1
    elif initial_tx < light_x and initial_ty < light_y:
        direction = "SE"
        initial_tx += 1
        initial_ty += 1
    elif initial_tx < light_x and initial_ty == light_y:
        direction = "E"
        initial_tx += 1
        initial_ty -= 0
    elif initial_tx < light_x and initial_ty > light_y:
        direction = "NE"
        initial_tx += 1
        initial_ty -= 1
    elif initial_tx == light_x and initial_ty > light_y:
        direction = "N"
        initial_tx += 0
        initial_ty -= 1
    
    # A single line providing the move to be made: N NE E SE S SW W or NW
    # N - North
    # S - South
    # W - West
    # E - East
    print(direction)
