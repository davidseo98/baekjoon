import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
ruby_list = list()
for _ in range(n):
    heapq.heappush(ruby_list, list(map(int, sys.stdin.readline().split())))

bag_list = [int(sys.stdin.readline()) for _ in range(k)]
bag_list.sort()

answer = 0
candidate = list()
for bag in bag_list:
    while ruby_list and bag >= ruby_list[0][0]:
        w, v = heapq.heappop(ruby_list)
        heapq.heappush(candidate, -v)
    if candidate:
        answer -= heapq.heappop(candidate)

print(answer)
