import sys

n, k = map(int, sys.stdin.readline().split())
dp_table = [0] * (n + 1)
dp_table[1], dp_table[2] = 1, 3
for i in range(3, n + 1):
    dp_table[i] = dp_table[i - 1] + dp_table[i - 2]
    if i == k:
        print(dp_table[k])
        break
