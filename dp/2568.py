import sys
import bisect

n = int(sys.stdin.readline())
a = list()
b = list()
for _ in range(n):
    n1, n2 = map(int, sys.stdin.readline().split())
    a.append(n1)
    b.append(n2)
line_list = [a, b]
dp = [[a[0]], [b[0]]]
dp_2 = [0] * (n + 1)
for i in range(1, n):
    if a[i - 1] < a[i] and b[i - 1] < b[i]:
        dp_2[i] = len(dp)
        dp[0].append(a[i])
        dp[1].append(b[i])
    else:
        dp_2[i] = min(bisect.bisect_left(dp[0], a[i]), bisect.bisect_left(dp[1], b[i]))
        dp[0][dp_2[i]] = a[i]
        dp[1][dp_2[i]] = b[i]

print(dp)
print(dp_2)
