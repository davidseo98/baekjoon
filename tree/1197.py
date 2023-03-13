import sys

def find(a):
    if parent[a] == a: return a
    return find(parent[a])

def union(a, b):
    a, b = find(a), find(b)
    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[a] = b
        rank[b] += 1

input = sys.stdin.readline

v, e = map(int, input().split())
edges = []
parent = {node : node for node in range(1, v + 1)}
rank = [1] * (v + 1)
answer = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(a) == find(b): continue

    union(a, b)
    answer += cost

print(answer)