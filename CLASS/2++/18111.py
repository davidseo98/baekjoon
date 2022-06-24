import sys

n, m, inventory = map(int, sys.stdin.readline().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

result = list()
best_time = 10000000000000
best_height = 0

for want_level in range(0, 257):
    blocks_added = 0
    blocks_removed = 0

    for i in range(n):
        for j in range(m):
            cur_level = graph[i][j]
            diff = cur_level - want_level

            if diff >= 0:
                blocks_removed += diff

            else:
                blocks_added -= diff

    if inventory + blocks_removed >= blocks_added:
        time = blocks_added + blocks_removed * 2
        if time <= best_time:
            best_time = time
            best_height = want_level

print(best_time, best_height)
