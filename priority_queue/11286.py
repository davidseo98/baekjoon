import heapq
import sys

n = int(input())
heap = list()

for i in range(n):
    in_value = int(sys.stdin.readline().rstrip())
    if in_value == 0:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
    else:
        heapq.heappush(heap, (abs(in_value), in_value))
