"""
백트래킹 -> 시간초과
다이나믹 프로그래밍 -> 실패 
"""

import sys

n = int(sys.stdin.readline())
dp = [[0] * 10 for _ in range(n)]
for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, n):
    for j in range(0, 10):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j + 1] + dp[i - 1][j - 1]

print(sum(dp[-1])%1000000000)
