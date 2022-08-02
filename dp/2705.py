import sys

t = int(sys.stdin.readline())
dp = [-1] * (1001)
dp[1], dp[2] = 1, 2
for i in range(3, 1001):
    div = i // 2
    dp[i] = 1 + sum(dp[1 : div + 1])
for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])
