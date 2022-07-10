import sys

n, k = map(int, sys.stdin.readline().split())
num_list = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0] * (k + 1)
dp[0] = 1

for num in num_list:
    for i in range(num, k + 1):
        if i >= num:
            dp[i] += dp[i - num]

print(dp[k])
