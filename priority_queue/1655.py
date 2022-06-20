import sys
import heapq
from collections import deque

n = int(sys.stdin.readline().rstrip())
front_heap = list()
back_heap = list()
front_count, back_count = 0, 0
for i in range(n):
    num = int(sys.stdin.readline().rstrip())

    if i == 0:
        front_heap.append(-num)
        front_count += 1
        print(num)
        continue

    front_max = -front_heap[0]

    if num > front_max:
        if front_count > back_count:
            heapq.heappush(back_heap, num)
            back_count += 1
        elif front_count == back_count:
            heapq.heappush(back_heap, num)
            heapq.heappush(front_heap, -heapq.heappop(back_heap))
            front_count += 1
    else:
        if front_count > back_count:
            heapq.heappush(front_heap, -num)
            heapq.heappush(back_heap, -heapq.heappop(front_heap))
            back_count += 1
        elif front_count == back_count:
            heapq.heappush(front_heap, -num)
            front_count += 1
    # print(front_heap, back_heap)
    print(-front_heap[0])
