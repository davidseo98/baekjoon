import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
line_dict = dict()
for i in range(1, n + 1):
    line_dict[i] = list()
for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    line_dict[n1].append(n2)
    line_dict[n2].append(n1)

visited = [0] * (n + 1)
count = 0

for key in line_dict.keys():
    if visited[key]:
        continue
    count += 1
    queue = deque([key])
    visited[key] = 1
    while queue:
        cur_value = queue.popleft()
        for value in line_dict[cur_value]:
            if not (visited[value]):
                visited[value] = 1
                queue.append(value)

print(count)
