import sys
from collections import deque


def bfs():
    global answer
    queue = deque()
    queue.append(subin)
    visited[subin] = 1
    while queue:
        cur = queue.popleft()
        if cur == target:
            print(visited[cur] - 1)
            break
        for next in [cur + 1, cur - 1, cur * 2]:
            if 0 <= next < 100001 and not visited[next]:
                visited[next] = True
                if next == cur * 2:
                    queue.appendleft(next)
                    visited[next] = visited[cur]
                else:
                    queue.append(next)
                    visited[next] = visited[cur] + 1


subin, target = map(int, sys.stdin.readline().split())
visited = [0] * (100001)
answer = list()
bfs()
