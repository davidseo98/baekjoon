from collections import defaultdict
import heapq

def dijkstra(start):
    distances = {node : float('inf') for node in range(1, n + 1)}
    distances[start] = 0

    heap = [(distances[start], start)]
    while heap:

        cur_dist, cur_node = heapq.heappop(heap)

        if cur_dist > distances[cur_node]: continue

        for next_node, next_dist in graph[cur_node].items():

            total_dist = cur_dist + next_dist
            if total_dist > distances[next_node]: continue

            distances[next_node] = total_dist
            heapq.heappush(heap, (total_dist, next_node))
    
    return distances

n, m, x = map(int, input().split())

graph = defaultdict(dict)
for _ in range(m):
    a, b, dist = map(int, input().split())
    graph[a][b] = dist

x_dists = dijkstra(x)

answer = 0
for node in range(1, n + 1):
    dist = dijkstra(node)[x] + x_dists[node]
    answer = max(answer, dist)

print(answer)