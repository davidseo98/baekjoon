import sys

dp = [[0] * 2001 for _ in range(2001)]
for i in range(2001):
    dp[0][i] = 1
for i in range(1, 2001):
    for j in range(1, 2001):
        dp[i][j] = dp[i][j - 1]
        if i >= j:
            dp[i][j] += dp[i - j][j - 1]

t = int(sys.stdin.readline())
for _ in range(t):
    num = int(sys.stdin.readline())
    print(dp[num][num] % 100999)
