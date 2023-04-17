
h, w = map(int, input().split())
board = [[0] * w for _ in range(h)]

for i, height in enumerate(map(int, input().split())):
    for row in range(h - 1, h - height - 1, -1):
        board[row][i] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0

for x in range(h - 1, -1, -1):
    wall_start, wall_end, empty_cnt = False, False, 0
    for y in range(w):

        if not wall_start and board[x][y]:
            wall_start = True
            continue
        
        if wall_start and board[x][y] == 0:
            empty_cnt += 1
            continue
        
        if wall_start and board[x][y] == 1:
            wall_end = True

            if wall_start and wall_end and empty_cnt:
                answer += empty_cnt
                empty_cnt = 0
                wall_end = False

print(answer)

