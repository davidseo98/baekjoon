import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
dp = [1] * n
dp_parent = [-1] * n
for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            if dp[i] > dp[j] + 1:
                continue
            else:
                dp[i] = dp[j] + 1
                dp_parent[i] = j

max_dp = max(dp)
print(max_dp)
max_dp_idx = dp.index(max_dp)
lis = list()
while max_dp_idx != -1:
    lis.append(num_list[max_dp_idx])
    max_dp_idx = dp_parent[max_dp_idx]

print(*sorted(lis))
