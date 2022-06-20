from heapq import *
import sys

n = int(sys.stdin.readline().rstrip())
heap = list()
for i in range(n):
    heappush(heap, int(sys.stdin.readline().rstrip()))

while heap:
    print(heappop(heap))
