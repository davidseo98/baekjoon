import sys

n = int(sys.stdin.readline())
graph = list()
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
dist_count = [[0] * n for _ in range(n)]
dist_count[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            break
        cur_cnt = graph[i][j]
        if j + cur_cnt < n:
            dist_count[i][j + cur_cnt] += dist_count[i][j]
        if i + cur_cnt < n:
            dist_count[i + cur_cnt][j] += dist_count[i][j]

print(dist_count[n - 1][n - 1])
