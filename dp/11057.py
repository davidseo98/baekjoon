import sys

n = int(sys.stdin.readline())
dp = [[0] * (10) for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(10):
        if i == 0:
            dp[i][j] = 1
            continue
        dp[i][j] = sum(dp[i - 1][j:]) % 10007

print(dp[-1][0])
