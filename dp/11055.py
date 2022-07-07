import sys
import copy

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
dp = copy.deepcopy(num_list)
for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j] + num_list[i])

print(max(dp))
