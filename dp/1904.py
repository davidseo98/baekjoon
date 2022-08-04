import sys

n = int(sys.stdin.readline())
if n == 1:
    print(1)
    exit()
if n == 2:
    print(2)
    exit()
memo = [0] * (n + 1)
memo[1], memo[2] = 1, 2
for i in range(3, n + 1):
    memo[i] = (memo[i - 1] + memo[i - 2]) % 15746

print(memo[n])
