import sys

n, k = map(int, sys.stdin.readline().split())
answer = 1
for _ in range(k):
    answer = (answer * n)
    n -= 1

while k:
    answer //= k
    k -= 1

print(answer % 10007)