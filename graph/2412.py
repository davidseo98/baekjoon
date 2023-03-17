# 그래프를 어떻게 만들 것인가 ?
# 1. 일단 좌표를 찍고, 이웃을 그래프에서 확인 -> 메모리 초과날 것 같음
# 2. 좌표 집합을 만들고, 범위안에 있는 좌표가 집합에 있는지 확인하면서 연결 확인

import sys
from collections import defaultdict, deque

def bfs():
    queue = deque([(0, 0, 0)])
    visited = set()
    visited.add((0, 0))

    while queue:
        x, y, cnt = queue.popleft()

        if x == top: return cnt

        for next in graph[(x, y)]:
            if next in visited: continue
            queue.append((next[0], next[1], cnt + 1))
            visited.add(next)

    return -1


input = sys.stdin.readline

n, top = map(int, input().split())
graph = defaultdict(list)
holes_set = {(0, 0)}

for _ in range(n):
    x, y = map(int, input().split())
    holes_set.add((y, x))

for hole in holes_set:
    x, y = hole
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if dx == 0 and dy == 0: continue
            if (x + dx, y + dy) in holes_set: graph[(x, y)].append((x + dx, y + dy))

print(bfs())
