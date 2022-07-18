import sys
import bisect

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
dp = [num_list[0]]
for i in range(1, n):
    if num_list[i] > dp[-1]:
        dp.append(num_list[i])
    else:
        idx = bisect.bisect_left(num_list[i], dp)
        dp[idx] = num_list[i]

print(len(dp))
