import heapq
import sys

n = int(sys.stdin.readline().rstrip())
heap = list()

for i in range(n):
    in_value = int(sys.stdin.readline().rstrip())
    if in_value == 0:
        try:
            print(-heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, -in_value)
