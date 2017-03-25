def validSolution(board):
    arr = []
    valid = []
    for i in range(27):
        arr.append([])

    #rows
    for i in range(9):
        arr[i] = board[i]
    
    #columns
    for i in range(9):
        for j in range(9):
            arr[i+9].append(board[j][i])
    
    #top_squares
    for j in range(3):
        for k in range(3):
            arr[18].append(board[j][k])
    for j in range(3, 6):
        for k in range(3):
            arr[19].append(board[j][k])
    for j in range(6, 9):
        for k in range(3):
            arr[20].append(board[j][k])
    
    #mid_squares
    for j in range(3):
        for k in range(3, 6):
            arr[21].append(board[j][k])
    for j in range(3, 6):
        for k in range(3, 6):
            arr[22].append(board[j][k])
    for j in range(6, 9):
        for k in range(3, 6):
            arr[23].append(board[j][k])
    
    #bot_squares
    for j in range(3):
        for k in range(6, 9):
            arr[24].append(board[j][k])
    for j in range(3, 6):
        for k in range(6, 9):
            arr[25].append(board[j][k])
    for j in range(6, 9):
        for k in range(6, 9):
            arr[26].append(board[j][k])
    
    for i in range(27):
        if arr[i].count(1) == 1 and arr[i].count(2) == 1 and arr[i].count(3) == 1 and arr[i].count(4) == 1 and arr[i].count(5) == 1 and arr[i].count(6) == 1 and arr[i].count(7) == 1 and arr[i].count(8) == 1 and arr[i].count(9) == 1:
            valid.append(True)
    
    if len(valid) == 27:
        return True
    return False
