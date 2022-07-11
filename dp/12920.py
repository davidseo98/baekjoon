import sys

n, m = map(int, sys.stdin.readline().split())
weight = list()
value = list()
count = list()
for _ in range(n):
    w, v, k = map(int, sys.stdin.readline().split())
    weight.append(w)
    value.append(v)
    count.append(k)

dp_table = [[0] * (m + 1) for _ in range(n + 1)]
dp_memory = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(1, m + 1):
        cur_count = min(w // weight[i - 1], count[i - 1])
        cur_weight = cur_count * weight[i - 1]
        if cur_weight <= w and cur_weight:
            dp_table[i][w] = max(
                [
                    dp_table[i - 1][w - x * weight[i - 1]] + x * value[i - 1]
                    for x in range(1, cur_count + 1)
                ]
                + [dp_table[i - 1][w]]
            )
        else:
            dp_table[i][w] = dp_table[i - 1][w]
            dp_memory[i][w] = dp_memory[i - 1][w]
print(dp_table[-1][-1])
