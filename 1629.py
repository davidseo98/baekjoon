import sys
from collections import deque

a, b, c = map(int, sys.stdin.readline().split())
rest = deque([0] * 2)
rest[0] = a % c
rest[1] = a**2 % c
for i in range(2, b):
    num = rest.popleft()
    rest.append((num * rest[0]) % c)

print(rest[-1])
