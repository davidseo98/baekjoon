import sys

MOD = 1000000000
n, k = map(int, sys.stdin.readline().split())
dp_table = [[0] * (n + 1) for _ in range(k + 1)]
dp_table[1][0] = 1
for i in range(k + 1):
    for j in range(n + 1):
        if i != 0 and j == 0:
            dp_table[i][j] = 1
for i in range(1, k + 1):
    for j in range(1, n + 1):
        dp_table[i][j] = (dp_table[i - 1][j] + dp_table[i][j - 1]) % MOD

print(dp_table[-1][-1])
