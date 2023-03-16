import sys

def move(board):
    temp = [[[] for _ in range(n)] for _ in range(n)]
    for row in board:
        for block in row:
            if not block: continue
            while block:
                r, c, m, s, d = block.pop()
                nr, nc = (r + s * dx[d]) % n, (c + s * dy[d]) % n
                temp[nr][nc].append([nr, nc, m, s, d])
    return temp

def fireball(board):
    for row in board:
        for block in row:
            if len(block) >= 2:
                nm, ns, cnt, nd = 0, 0, len(block), [1, 3, 5, 7]
                is_odd, is_even = True, True
                while block:
                    r, c, m, s, d = block.pop()
                    if d % 2 == 0: is_odd = False
                    if d % 2 == 1: is_even = False

                    nm += m
                    ns += s
                
                if nm < 5: continue
                nm = nm // 5
                ns = ns // cnt

                if is_odd or is_even: nd = [0, 2, 4, 6]

                for _s in nd:
                    block.append([r, c, nm, ns, _s])
    return board

input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]

dy = [0, 1, 1, 1, 0, -1, -1, -1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    board[r - 1][c - 1].append([r - 1, c - 1, m, s, d])

for _ in range(k):
    board = move(board)
    board = fireball(board)

answer = 0
for row in board:
    for block in row:
        for element in block:
            answer += element[2]

print(answer)