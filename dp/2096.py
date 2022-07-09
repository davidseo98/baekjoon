import sys

n = int(sys.stdin.readline())
max_dp = [0] * 3
min_dp = [0] * 3
max_temp = [0] * 3
min_temp = [0] * 3

for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    for j in range(3):
        if j == 0:
            max_temp[j] = a + max(max_dp[0], max_dp[1])
            min_temp[j] = a + min(min_dp[0], min_dp[1])
        elif j == 1:
            max_temp[j] = b + max(max_dp[0], max_dp[1], max_dp[2])
            min_temp[j] = b + min(min_dp[0], min_dp[1], min_dp[2])
        else:
            max_temp[j] = c + max(max_dp[1], max_dp[2])
            min_temp[j] = c + min(min_dp[1], min_dp[2])

    for j in range(3):
        max_dp[j], min_dp[j] = max_temp[j], min_temp[j]

print(max(max_dp), min(min_dp))
