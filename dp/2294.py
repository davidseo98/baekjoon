import sys

n, k = map(int, sys.stdin.readline().split())
num_list = [int(sys.stdin.readline()) for _ in range(n)]
dp = [10001] * (k + 1)
dp[0] = 0
for i in range(len(num_list)):
    for j in range(num_list[i], k + 1):
        dp[j] = min(dp[j], dp[j - num_list[i]] + 1)

if dp[-1] != 10001 :
    print(dp[-1])
else :
    print(-1)
