import sys

n = int(sys.stdin.readline())
dp = list(range(n + 1))
i = 1
while i**2 < n + 1:
    for j in range(i**2, n + 1):
        dp[j] = min(dp[j - i**2] + 1, dp[j])
    i += 1
print(dp[-1])
