import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append((target1, 1))
    visited[target1] = True
    while queue:
        cur, cnt = queue.popleft()
        for next in relation_dict[cur]:
            if not visited[next]:
                if next == target2:
                    print(cnt)
                    exit()
                visited[next] = True
                queue.append((next, cnt + 1))
    print(-1)


n = int(sys.stdin.readline())
target1, target2 = map(int, sys.stdin.readline().split())
n_rel = int(sys.stdin.readline())
relation_dict = dict()
for _ in range(n_rel):
    parent, child = map(int, sys.stdin.readline().split())
    if parent in relation_dict.keys():
        relation_dict[parent].append(child)
    else:
        relation_dict[parent] = [child]
    if child in relation_dict.keys():
        relation_dict[child].append(parent)
    else:
        relation_dict[child] = [parent]
visited = [False] * (n + 1)

bfs()
