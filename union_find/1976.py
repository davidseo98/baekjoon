import sys

def find(node):
    if parent[node] == node: return node
    else: return find(parent[node])

def union(node1, node2):
    global parent, rank
    r1, r2 = find(node1), find(node2)
    if r1 == r2 : return
    if rank[r1] >= rank[r2]:
        parent[r1] = r2
        rank[r2] += rank[r1]
    else:
        parent[r2] = r1
        rank[r1] += rank[r2]
    

input = sys.stdin.readline

n = int(input())
m = int(input())
rank = [1] * (n + 1)
parent = dict()
for node in range(1, n + 1):
    parent[node] = node

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j]: union(i + 1, j + 1)

path = list(map(int, input().split()))
roots = [find(x) for x in path]
for i in range(len(roots) - 1):
    if roots[i] != roots[i + 1]:
        print("NO")
        exit()
print("YES")
