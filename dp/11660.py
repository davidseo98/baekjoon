import sys


def dim_reduction(x, y):
    global n
    return (y - 1) * n + x


n, m = map(int, sys.stdin.readline().split())
graph = list()
for _ in range(n):
    graph += list(map(int, sys.stdin.readline().split()))

dp = [0] * (n * n + 1)

for i in range(n * n):
    if i == 0:
        dp[i + 1] = graph[i]
    else:
        dp[i + 1] = dp[i] + graph[i]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    start = dim_reduction(x1, y1)
    end = dim_reduction(x2, y2)
    print(start, end, dp[start], dp[end])
    print(dp[end] - dp[start - 1])
print(graph, len(graph))
print(dp, len(dp))
