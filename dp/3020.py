import sys

n, h = map(int, sys.stdin.readline().split())
is_odd = True
lower_dp = [0] * (h + 1)
upper_dp = [0] * (h + 1)
total_dp = [0] * (h + 1)
min_break = n
count = 0
for i in range(1, n + 1):
    num = int(sys.stdin.readline())
    if is_odd:
        lower_dp[num] += 1
    else:
        upper_dp[h - num + 1] += 1
    is_odd = not (is_odd)

for i in range(h, 0, -1):
    lower_dp[i - 1] += lower_dp[i]
for i in range(1, h + 1):
    upper_dp[i] += upper_dp[i - 1]
for i in range(1, h + 1):
    total_dp[i] = upper_dp[i] + lower_dp[i]
value = min(total_dp[1:])
print(value, total_dp.count(value))
