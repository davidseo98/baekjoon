import sys
import heapq

n = int(sys.stdin.readline())
assignment_list = []
for _ in range(n):
    t, point = map(int, sys.stdin.readline().split())
    heapq.heappush(assignment_list, (-t, point))
answer = 0
for i in range(n, 0, -1):
    candidate = list()
    while assignment_list and i <= -assignment_list[0][0]:
        t, point = heapq.heappop(assignment_list)
        heapq.heappush(candidate, (-point, t))
    if candidate:
        answer -= heapq.heappop(candidate)[0]
        while candidate:
            point, t = heapq.heappop(candidate)
            heapq.heappush(assignment_list, (t, -point))
print(answer)
