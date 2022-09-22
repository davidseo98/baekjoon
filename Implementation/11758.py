import sys


points = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

if points[0][0] == points[1][0]:
    slope = "y_line"
elif points[0][1] == points[1][1]:
    slope = "x_line"
else:
    slope = (points[0][1] - points[1][1]) / (points[0][0] - points[1][0])


if slope == "y_line":
    dir = points[1][1] - points[0][1]
    if points[2][0] == points[0][0]:
        print(0)
    elif points[2][0] > points[0][0]:
        if dir > 0:
            print(-1)
        else:
            print(1)
    else:
        if dir > 0:
            print(1)
        else:
            print(-1)

elif slope == "x_line":
    dir = points[1][0] - points[0][0]
    if points[2][1] == points[0][1]:
        print(0)
    elif points[2][1] > points[0][1]:
        if dir > 0:
            print(1)
        else:
            print(-1)
    else:
        if dir > 0:
            print(-1)
        else:
            print(1)

else:
    y_intercept = points[0][1] - slope * points[0][0]
    y_value = points[2][0] * slope + y_intercept
    dir = points[1][0] - points[0][0]

    if y_value == points[2][1]:
        print(0)

    elif y_value > points[2][1]:
        if dir > 0:
            print(-1)
        elif dir < 0:
            print(1)
        else:
            pass

    else:
        if dir < 0:
            print(-1)
        elif dir > 0:
            print(1)

# print(y_value, points[2], dir)
