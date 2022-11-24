import sys

def dfs(sx, sy, len):
    global ONE, ZERO, MINUS
    init_val = graph[sx][sy]
    for i in range(sx, sx + len):
        for j in range(sy, sy + len):
            if graph[i][j] != init_val:
                n_len = len // 3
                for next in [[sx, sy], [sx, sy + n_len], [sx, sy + 2*n_len],
                             [sx + n_len, sy], [sx + n_len, sy + n_len], [sx + n_len, sy + 2*n_len],
                             [sx + 2*n_len, sy], [sx + 2*n_len, sy + n_len], [sx + 2*n_len, sy + 2*n_len]] :
                    dfs(next[0], next[1], n_len)
                return

    if init_val == 1: ONE += 1
    elif init_val == 0: ZERO += 1
    else: MINUS += 1

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ONE, ZERO, MINUS = 0, 0, 0

dfs(0, 0, n)

print(MINUS)
print(ZERO)
print(ONE)
