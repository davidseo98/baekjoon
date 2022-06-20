from heapq import *
import sys

n = int(sys.stdin.readline().rstrip())
heap = list()
for _ in range(n):
    heappush(heap, -int(sys.stdin.readline().rstrip()))

while heap:
    print(-heappop(heap))
