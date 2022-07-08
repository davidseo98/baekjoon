import sys

n, m = map(int, sys.stdin.readline().split())
weight = list()
value = list()
total_item_count = 0
for _ in range(n):
    w, v, k = map(int, sys.stdin.readline().split())
    for _ in range(k):
        weight.append(w)
        value.append(v)
        total_item_count += 1
dp_table = [[0] * (m + 1) for _ in range(total_item_count + 1)]
for i in range(1, total_item_count + 1):
    for w in range(1, m + 1):
        if weight[i - 1] > w:
            dp_table[i][w] = dp_table[i - 1][w]
        else:
            dp_table[i][w] = max(
                value[i - 1] + dp_table[i - 1][w - weight[i - 1]], dp_table[i - 1][w]
            )
print(dp_table[-1][-1])
