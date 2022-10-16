from re import L
import sys


points = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
slopes = list()
for i in range(1, 3):
    dx = points[i][0] - points[i - 1][0]
    dy = points[i][1] - points[i - 1][1]
    if dx == 0:
        slopes.append("vertical_line")
        continue
    if dy == 0:
        slopes.append("horizontal_line")
        continue

    slopes.append(dy / dx)

if slopes[0] == slopes[1]:
    print(0)
    exit()

if slopes[0] == "horizontal_line":
    if points[0][0] < points[1][0]:
        if points[1][1] < points[2][1]:
            print(1)
        else:
            print(-1)

    else:
        if points[1][1] < points[2][1]:
            print(-1)
        else:
            print(1)

if slopes[0] == "vertical_line":
    if points[0][1] > points[1][1]:
        if points[1][0] < points[2][0]:
            print(1)
        else:
            print(-1)

    else:
        if points[1][1] < points[2][1]:
            print(-1)
        else:
            print(1)

else:
    decide = (points[0][0] - points[1][0]) * (points[1][1] - points[2][1]) - (
        points[1][0] - points[2][0]
    ) * (points[1][1] - points[2][1])
    if decide == 0:
        print(0)
        exit()

    if slopes[0] > 0:
        if slopes[1] > 0:
            if decide < 0:
                print(1)
            
        else:
            if points[1][1] < points[2][1]:
                print(1)
            else:
                print(-1)

    else:
        if slopes[1] < 0:
            if decide > 0:
                print(-1)
            else:
                print(1)
        else:
            if points[1][1] < points[2][1]:
                print(-1)
            else:
                print(1)


# print(slopes)
