import sys

n, total_weight = map(int, sys.stdin.readline().split())
weights = list()
values = list()
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    weights.append(w)
    values.append(v)
dp_table = [[0] * (total_weight + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, total_weight + 1):
        if weights[i - 1] <= w:
            dp_table[i][w] = max(
                values[i - 1] + dp_table[i - 1][w - weights[i - 1]], dp_table[i - 1][w]
            )
        else:
            dp_table[i][w] = dp_table[i - 1][w]
print(dp_table[-1][-1])
