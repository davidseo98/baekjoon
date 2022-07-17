from collections import deque


def bfs():
    queue = deque()
    queue.append((n, 0))
    visited[n] = True

    while queue:
        cur, cnt = queue.popleft()
        if cur == m:
            return cnt + 1

        for next in [cur * 2, int(str(cur) + "1")]:
            if 0 <= next <= m and not visited[next]:
                queue.append((next, cnt + 1))
                visited[next] = True

    return -1


n, m = map(int, input().split())
visited = [False] * (m + 1)
print(bfs())
