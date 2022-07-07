import sys
import bisect
import copy

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
dp = [num_list[0]]
dp_2 = [0] * n
for i in range(n):
    if num_list[i] > dp[-1]:
        dp.append(num_list[i])
        dp_2[i] = len(dp)
    else:
        dp_2[i] = bisect.bisect_left(dp, num_list[i])
        dp[dp_2[i]] = num_list[i]
print(dp_2)
max_dp = max(dp_2)
max_dp_idx = dp_2.index(max_dp)
lis = list()
for i in range(n - 1, -1, -1):
    print(max_dp)
    if dp_2[i] == max_dp:
        lis.append(num_list[i])
        max_dp -= 1


print(len(lis))
print(*sorted(lis))
