import sys

n = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(n)]
if n < 3:
    print(sum(num_list))
    exit()
dp = [0] * (n + 1)
dp[1] = num_list[0]
dp[2] = num_list[1] + num_list[0]
for i in range(3, n + 1):
    dp[i] = num_list[i - 1] + max(dp[i - 3] + num_list[i - 2], dp[i - 2])
print(dp[-1])
