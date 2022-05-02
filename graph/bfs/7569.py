from collections import deque

x, y, z = map(int, input().split())

graph = list()
for i in range(z):
    l = list()
    for j in range(y):
        ll = list(map(int, input().split()))
        l.append(ll)
    graph.append(l)

queue = deque()
for i in range(z):
    for j in range(y):
        for m in range(x):
            if graph[i][j][m] == 1:
                queue.append((i, j, m))


def bfs():

    dh = [0, 0, 0, 0, 1, -1]
    dm = [0, 0, 1, -1, 0, 0]
    dn = [1, -1, 0, 0, 0, 0]

    while queue:
        h, n, m = queue.popleft()
        for i in range(6):
            nh, nn, nm = h + dh[i], n + dn[i], m + dm[i]

            if -1 < nh < z and -1 < nn < y and -1 < nm < x and graph[nh][nn][nm] == 0:
                graph[nh][nn][nm] = graph[h][n][m] + 1
                queue.append((nh, nn, nm))


bfs()

maxes = list()
for i in range(z):
    for j in range(y):
        for m in range(x):
            if graph[i][j][m] == 0:
                print(-1)
                exit()
        maxes.append(max(graph[i][j]))

print(max(maxes) - 1)
