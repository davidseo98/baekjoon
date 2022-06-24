import sys

n = int(sys.stdin.readline())
coordinates = list()
for _ in range(n):
    coordinates.append(list(map(int, sys.stdin.readline().split())))

coordinates.sort()
coordinates.sort(key=lambda x: x[1])

for c in coordinates:
    print(c[0], c[1])
