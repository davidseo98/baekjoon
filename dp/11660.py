import sys

n, m = map(int, sys.stdin.readline().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(n):
        dp[i][j + 1] = dp[i][j] + graph[i - 1][j]
for i in range(1, n + 1) :
    for j in range(n) :
        dp[j + 1][i] = dp[j][i] + dp[j + 1][i]

for _ in range(m):
    value = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    value = dp[x2][y2] - dp[x2][y1-1] - (dp[x1-1][y2] - dp[x1-1][y1-1])
    print(value)
