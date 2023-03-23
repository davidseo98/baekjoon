import sys, math, heapq
from collections import defaultdict

def prim():

    visited = [False] * (n + 1)
    visited[1] = True
    mst = []
    candidates = []
    for key, item in neighbors[1].items():
        heapq.heappush(candidates, (item, key))

    while candidates:
    
        dist, next_node = heapq.heappop(candidates)

        if not visited[next_node]:
            
            visited[next_node] = True
            mst.append((dist, next_node))
            
            for node, dist in neighbors[next_node].items():
                if not visited[node]:
                    heapq.heappush(candidates, (dist, node))
    return mst

input = sys.stdin.readline

n, m = map(int, input().split())
nodes = []
neighbors = defaultdict(dict)
connections = defaultdict(list)

for node in range(1, n + 1):
    x, y = map(int, input().split())
    nodes.append((node, x, y))

for cn, cx, cy in nodes:
    for on, ox, oy in nodes:
        if on == cn: continue # 스스로와 간선 x
        dist = math.sqrt((cx - ox) ** 2 + (cy - oy) ** 2)
        neighbors[cn][on] = dist

for _ in range(m):
    n1, n2 = map(int, input().split())
    neighbors[n1][n2] = 0 
    neighbors[n2][n1] = 0

answer = 0

for dist, _ in prim():
    answer += dist 

print(format(answer,".2f"))
