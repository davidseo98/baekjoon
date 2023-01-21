import sys

def union(n1, n2):
    global parent
    x = find(n1)
    y = find(n2)
    if x == y: return

    if rank[x] >= rank[y]:
        parent[y] = x
        rank[x] += rank[y]
    else: 
        parent[x] = y
        rank[y] += rank[x]

def find(n):
    global parent
    if parent[n] == n: return n
    else: return find(parent[n])

input = sys.stdin.readline

n, m = map(int, input().split())

parent = dict()
rank = [1] * (n + 1)
for node in range(n + 1):
    parent[node] = node

for _ in range(m):
    t, node1, node2 = map(int, input().split())

    if t:
        print("YES") if find(node1) == find(node2) else print("NO")
    else:
        union(node1, node2)
