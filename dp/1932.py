import sys

n = int(sys.stdin.readline())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n-1) :
    for j in range(i + 2) :
        value = -1
        if 0 <= j <= i :
            value = triangle[i][j]
        if 0 <= j - 1 <= i :
            if triangle[i][j - 1] > value :
                value = triangle[i][j - 1]

        triangle[i + 1][j] += value

print(max(triangle[-1]))
