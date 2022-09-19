from re import L
import sys


coordinates = list()
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    coordinates.append((x, y))

relative_slopes = list()
absolute_slopes = list()
for i in range(3):
    cx, cy = coordinates[i]
    if cx == 0:
        absolute_slopes.append(float("inf"))
        continue
    coordinates.append(cx / cy)
for i in range(1, 3):
    cx, cy = coordinates[i]
    px, py = coordinates[i - 1]
    dx, dy = cx - px, cy - py
    if dx == 0:
        relative_slopes.append(float("inf"))
        continue
    relative_slopes.append(dy / dx)

if relative_slopes[1] == relative_slopes[0]:
    print(0)
    exit()

if slopes[0] >= 0:
    if slopes[0] > slopes[1]:
        print(-1)
    else:
        print(1)
else:
    if slopes[0] < slopes[1]:
        print(1)
    else:
        print(1)
