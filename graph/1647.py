import sys

def find(a):
    if parent[a] == a: return a
    else: return find(parent[a])

def union(a, b):
    a, b = find(a), find(b)
    if a == b: return

    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        rank[b] += 1

input = sys.stdin.readline

answer = 0
n, m = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]
parent = {node : node for node in range(1, n + 1)}
rank = [1] * (n + 1)

roads.sort(key = lambda x : x[2])
last = -1
for road in roads:

    a, b, cost = road
    if find(a) == find(b): continue

    union(a, b)
    answer += cost
    last = cost

print(answer - last)