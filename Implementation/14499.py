import sys

def move(x, y, t):
    global dice, board

    dx, dy = movement[t]
    nx, ny = x + dx, y + dy

    if not(0 <= nx < n) or not(0 <= ny < m): 
        return x, y

    if t == 1:
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
    
    elif t == 2:
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
    
    elif t == 3:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
    
    else:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
    

    print(dice[1][1])

    if board[nx][ny]:
        dice[3][1] = board[nx][ny]
        board[nx][ny] = 0
    else:
        board[nx][ny] = dice[3][1]

    return nx, ny
input = sys.stdin.readline

n, m, x, y, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dice = [[0] * 3 for _ in range(4)]

movement = {1 : (0, 1), 2 : (0, -1), 3 : (-1, 0), 4 : (1, 0)}

for t in map(int, input().split()):
    x, y = move(x, y, t)

