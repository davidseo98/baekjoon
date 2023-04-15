from collections import defaultdict, deque

def simulate(v):
    global board, viruses, virus_cnt

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque(viruses[v])

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                board[nx][ny] = v
                viruses[v].append((nx, ny))
                virus_cnt += 1

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, tx, ty = map(int, input().split())

viruses = defaultdict(list)
virus_cnt = 0
for x in range(n):
    for y in range(n):
        if board[x][y]: 
            virus_cnt += 1
            viruses[board[x][y]].append((x, y))

stop_flag = False
for _ in range(s):
    for v in range(1, k + 1):
        if virus_cnt >= n ** 2: 
            stop_flag = True
            break
        simulate(v)

    if stop_flag: break

print(board[tx - 1][ty - 1])
