import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
ruby_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
bag_list = [int(sys.stdin.readline()) for _ in range(k)]
bag_list.sort()
# heapq.heapify(ruby_list)
answer = 0
for bag in bag_list:
    candidate = list()
    while ruby_list and ruby_list[0][0] <= bag:
        w, v = heapq.heappop(ruby_list)
        heapq.heappush(candidate, (-v, w))
    if candidate:
        answer -= heapq.heappop(candidate)[0]
        while candidate:
            v, w = heapq.heappop(candidate)
            heapq.heappush(ruby_list, (w, -v))
print(answer)
