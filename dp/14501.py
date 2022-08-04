import sys

n = int(sys.stdin.readline())
p_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [0] * (n + 1)
for i in range(n):
    duration, price = p_list[i][0], p_list[i][1]
    if i + duration <= n:
        for j in range(i + duration, n + 1):
            dp[j] = max(dp[j], dp[i] + price)
print(max(dp))
