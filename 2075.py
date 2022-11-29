import sys 
import heapq

n = int(sys.stdin.readline()) 

for i in range(n):
    num_list = list(map(int, sys.stdin.readline().split()))
    if i == 0:
        heap = num_list
        heapq.heapify(heap)
        continue

    for num in num_list:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

print(heap[0])