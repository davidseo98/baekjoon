import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))
print(len(a - b))
diff = list(a - b)
heapq.heapify(diff)

while diff:
    print(heapq.heappop(diff), end=" ")
