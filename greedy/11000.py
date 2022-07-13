import sys
import heapq

n = int(sys.stdin.readline())
classes = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
classes.sort(key=lambda x: x[1])
classes.sort()
answer = 1
heap = [classes[0][1]]
cur_end = 0
for i in range(1, n):
    nw_class = classes[i]
    cur_end = max(cur_end, nw_class[0])
    while heap and heap[0] <= cur_end:
        heapq.heappop(heap)
    heapq.heappush(heap, nw_class[1])
    answer = max(answer, len(heap))
print(answer)
