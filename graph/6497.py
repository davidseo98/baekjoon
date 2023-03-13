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
        rank[a] += 1
        parent[b] = a

input = sys.stdin.readline

m, n = map(int, input().split())

while m or n:

    total, needed = 0, 0
    parent = {node : node for node in range(m)}
    rank = [1] * m
    roads = [list(map(int, input().split())) for _ in range(n)]
    roads.sort(key = lambda x : x[2])

    for road in roads:
        a, b, cost = road
        total += cost

        if find(a) == find(b): continue

        needed += cost
        union(a, b)
    print(total - needed)
    m, n = map(int, input().split())