import sys

n, k = map(int, sys.stdin.readline().split())
num_list = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0] * (k + 1)
count = [1] * (k + 1)
dp[0], count[0] = 1, 1

for num in num_list:
    for i in range(num, k + 1):
        if i >= num:
            dp[i] += dp[i - num]
            count[i] = min(count[i], count[i - num] + 1)
print(dp)
print(count)
