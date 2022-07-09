import sys

n, m = map(int, sys.stdin.readline().split())
memory = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
limit = sum(cost)
dp_table = [[0] * (limit + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(1, limit + 1):
        if cost[i - 1] > w:
            dp_table[i][w] = dp_table[i - 1][w]
        else:
            dp_table[i][w] = max(
                memory[i - 1] + dp_table[i - 1][w - cost[i - 1]], dp_table[i - 1][w]
            )
result = list()
for i in range(n + 1):
    for j in range(limit + 1):
        if dp_table[i][j] >= m:
            result.append(j)
print(min(result))
