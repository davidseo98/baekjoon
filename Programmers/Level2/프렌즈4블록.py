def find_sur(board, x, y):
    coor = [(x, y)]
    cur = board[x][y]
    bottom, left, corner, height = -1, -1, -1, 1
    for i in range(x + 1, len(board)):
        if board[i][y] != 'X':
            height += 1
            if bottom == -1: 
                bottom = board[i][y]
                coor.append((i, y))
    
    cnt = 0

    for i in range(len(board) - 1,  -1, -1):
        if board[i][y + 1] != 'X': cnt += 1
        
        if cnt == height and left == -1: 
            left = board[i][y + 1]
            coor.append((i, y + 1))
        if cnt == height - 1 and corner == -1:  
            corner = board[i][y + 1]
            coor.append((i, y + 1))

    if cur == bottom and bottom == corner and corner == left:
        return (coor)
    
    return []
    

def solution(m, n, board):
    answer = 0
    changed = True
    board = [list(board[i]) for i in range(m)]
    
    while changed:
        changed = False
        coor = []
        
        for i in range(m):
            for j in range(n - 1):
                if board[i][j] == "X": continue
                result = find_sur(board, i, j)
                if result:
                    changed = True
                    coor += result

        for c in set(coor):
            board[c[0]][c[1]] = 'X'
            answer += 1

    return answer