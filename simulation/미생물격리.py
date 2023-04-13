
def move(board, n, i):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    boundary = [0, n - 1]
    for x in range(n):
        for y in range(n):
            if board[x][y] and board[x][y][0][2]:

                cnt, d, _ = board[x][y].popleft()
                nx, ny = x + dx[d], y + dy[d]

                if nx in boundary or ny in boundary: # 경계에 도달한 경우
                    if d == 0 or d == 2:
                        d += 1
                    else:
                        d -= 1
                    cnt //= 2

                if cnt: board[nx][ny].append([cnt, d, 0])
def combine(board, n):
    for x in range(n):
        for y in range(n):
            if len(board[x][y]) == 1:
                board[x][y][0][2] = 1
            elif len(board[x][y]) > 1:
                max_cnt = -1
                cnt_sum = 0
                while board[x][y]:
                    cnt, d, _ = board[x][y].pop()
                    cnt_sum += cnt
                    if cnt > max_cnt :
                        nd = d
                        max_cnt = cnt
                board[x][y].append([cnt_sum, nd, 1])

from collections import deque

T = int(input())

for test_case in range(1, T + 1):

    n, m, k = map(int, input().split())
    board = [[deque([]) for _ in range(n)] for _ in range(n)]

    for _ in range(k):
        x, y, cnt, d = map(int, input().split())
        board[x][y].append([cnt, d - 1, 1])

    for i in range(m):

        move(board, n, i)
        combine(board, n)

    answer = 0
    for x in range(n):
        for y in range(n):
            if board[x][y]:
                cnt, _, _ = board[x][y][0]
                answer += cnt

    print(f"#{test_case} {answer}")