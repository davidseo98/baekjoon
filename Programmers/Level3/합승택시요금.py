from collections import deque
import heapq

def dijkstra(n, start, graph):
    
    distances = { i : float('inf') for i in range(1, n + 1)}
    distances[start] = 0
    
    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        if cur_dist > distances[cur_node]: continue
        
        for next_node, next_dist in graph[cur_node].items():
            total_dist = cur_dist + next_dist
            if total_dist < distances[next_node]:
                distances[next_node] = total_dist
                heapq.heappush(queue, [total_dist, next_node])
    
    return distances
    
def solution(n, s, a, b, fares):
    answer = float('inf')
    graph = { i : {} for i in range(1, n + 1)}
    node2dist = {}
    
    for f in fares:
        graph[f[0]][f[1]] = f[2]
        graph[f[1]][f[0]] = f[2]
    
    for node in range(1, n + 1):
        node2dist[node] = dijkstra(n, node, graph)
    
    for node in range(1, n + 1):
        fee = node2dist[s][node] + node2dist[node][a] + node2dist[node][b]
        answer = min(answer, fee)

    return answer