import sys
import heapq

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
heap = list()
for i in range(n):
    heapq.heappush(heap, (-num_list[i], i))

answer = 0
while heap:
    answer += 1
    cur_arrow, cur_loc = heapq.heappop(heap)
    while heap[0][0] == cur_arrow + 1 :
        