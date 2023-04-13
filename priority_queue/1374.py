import sys, heapq

input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
    num, start, end = map(int, input().split())
    heapq.heappush(classes, (start, end, num))

answer = 0
cur_classes = []

while classes:

    s, e, n = heapq.heappop(classes)

    while cur_classes and cur_classes[0] <= s:
        heapq.heappop(cur_classes)
    
    heapq.heappush(cur_classes, e)
    answer = max(answer, len(cur_classes))

print(answer)