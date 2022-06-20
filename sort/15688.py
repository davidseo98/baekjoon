import sys

n = int(sys.stdin.readline().rstrip())
heap = list()
for _ in range(n):
    heap.append(int(sys.stdin.readline().rstrip()))

for num in sorted(heap):
    print(num)
