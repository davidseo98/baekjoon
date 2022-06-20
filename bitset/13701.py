import sys
from collections import deque

l = list(map(bin, map(int, sys.stdin.readline().rstrip().split())))
visited = set()
for num in l:
    if num not in visited:
        print(int(num[2:], 2), end=" ")
        visited.add(num)
