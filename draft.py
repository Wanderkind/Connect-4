
no, ht, bn = 7, 6, 4
# original: 7, 6, 4

board = [[0 for _ in range(ht)] for _ in range(no)]

def four(board, p):

    ideal = [p for _ in range(bn)]
    
    for i in board:
        for j in range(ht - bn + 1):
            if i[j:j + bn] == ideal:
                return True
    
    for i in range(ht):
        for j in range(no - bn + 1):
            if [board[j + k][i] for k in range(bn)] == ideal:
                return True
    
    for i in range(ht - bn + 1):
        for j in range(no - bn + 1):
            if [board[j + k][i + k] for k in range(bn)] == ideal:
                return True
    
    for i in range(ht - bn + 1):
        for j in range(no - bn + 1):
            if [board[j + ht - bn + 1 - k][i + k] for k in range(bn)] == ideal:
                return True
    
    return False

def add(board, file, p): # assumes file is not full
    
    i = 0
    while board[file][i]:
        i += 1
    
    board[file][i] = p
    return board

def win(board, p, lst):
    
    print(lst) #######
    #for q in board:print(q)
    
    for i in range(no):
        if not [i[:] for i in board][i][-1]:
            if four(add([i[:] for i in board], i, p), p):
                return lst + [i + 1]
    
    for i in range(no):
        if not [i[:] for i in board][i][-1]:
            if win(add([i[:] for i in board], i, p), 3 - p, lst + [(i + 1)*(1 if p == 1 else -1)]) == -1:
                return lst + [i + 1]
    
    return -1

b = [[0 for _ in range(ht)] for _ in range(no)]

win(b, 1, [])
