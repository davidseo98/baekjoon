import sys
from itertools import combinations


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
chickens, houses = list(), list()
for y in range(n):
    for x in range(n):
        if graph[y][x] == 1:
            houses.append((x, y))
        elif graph[y][x] == 2:
            chickens.append((x, y))
answer = list()
for candidate in combinations(chickens, m):
    result = list()
    for house in houses:
        min_dist = 999
        for chicken in candidate:
            min_dist = min(
                min_dist, abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            )
        result.append(min_dist)
    answer.append(sum(result))
print(min(answer))
