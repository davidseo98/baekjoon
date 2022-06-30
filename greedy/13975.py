import sys
import heapq

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(files)
    result = 0
    while 1:
        if len(files) == 1:
            break
        num1 = heapq.heappop(files)
        num2 = heapq.heappop(files)
        result += num1 + num2
        heapq.heappush(files, num1 + num2)

    print(result)
