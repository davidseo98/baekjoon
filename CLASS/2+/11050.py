import sys

n, m = map(int, sys.stdin.readline().split())

if m == 0:
    print(1)
    exit()

result = n
for _ in range(m - 1):
    result *= n - 1
    n -= 1

while m > 1:
    result /= m
    m -= 1

print(int(result))
