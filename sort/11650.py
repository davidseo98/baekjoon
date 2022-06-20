import sys

n = int(sys.stdin.readline().rstrip())
coordinates = list()
for _ in range(n):
    coordinates.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

coordinates.sort(key=lambda x: x[1])
coordinates.sort(key=lambda x: x[0])

for c in coordinates:
    print(c[0], c[1])
