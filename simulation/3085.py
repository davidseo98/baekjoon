import sys

def simulate(board, cx, cy, nx, ny):

    max_cnt = 0
    results = [1] * 4
    for y in range(1, n):
        if board[cx][y] == board[cx][y - 1]:
            results[0] += 1
        else:
            results[0] = 0
        
        if board[nx][y] == board[nx][y - 1]:
            results[1] += 1
        else:
            results[1] = 0
        max_cnt = max(max_cnt, results[0], results[1])
    
    for x in range(1, n):
        if board[x][cy] == board[x - 1][cy]: results[2] += 1
        else: results[2] = 0

        if board[x][ny] == board[x - 1][ny]: results[3] += 1
        else: results[3] = 0
        max_cnt = max(max_cnt, results[2], results[3])

    return max_cnt

def simulate2(board):
    global answer
    for i in range(n):
        cnts = [1, 1]
        for row in range(1, n):
            if board[row][i] == board[row - 1][i]:
                cnts[0] += 1
            else:
                cnts[0] = 1
            answer = max(answer, cnts[0])

        for col in range(1, n):
            if board[i][col] == board[i][col - 1]:
                cnts[1] += 1
            else:
                cnts[1] = 1
            answer = max(answer, cnts[1])

input = sys.stdin.readline

n = int(input())

board = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
for i in range(n):
    cnts = [1, 1]
    for row in range(1, n):
        if board[row][i] == board[row - 1][i]:
            cnts[0] += 1
        else:
            cnts[0] = 1
        answer = max(answer, cnts[0])

    for col in range(1, n):
        if board[i][col] == board[i][col - 1]:
            cnts[1] += 1
        else:
            cnts[1] = 1
        answer = max(answer, cnts[1])

for x in range(n):
    for y in range(n):
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[x][y] != board[nx][ny]:
                
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                #nswer = max(answer, simulate(board, x, y, nx, ny))
                simulate2(board)
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]

print(answer)