import sys
import heapq

n_city, n_bus = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = dict()
for _ in range(n_bus):
    s, e, p = map(int, sys.stdin.readline().split())
    if s in graph.keys():
        graph[s].append((e, p))
    else:
        graph[s] = [(e, p)]

distance = {node: float("inf") for node in range(1, n_city + 1)}
distance[start] = 0
queue = list()
heapq.heappush(queue, [distance[start], start])
while queue:
    cur_price, cur_loc = heapq.heappop(queue)
    if distance[cur_loc] < cur_price:
        continue
    if cur_loc in graph.keys():
        for next_loc, price in graph[cur_loc]:
            next_price = price + cur_price
            if next_price < distance[next_loc]:
                distance[next_loc] = next_price
                heapq.heappush(queue, [distance[next_loc], next_loc])

for i in range(1, n_city + 1):
    if distance[i] == float("inf"):
        print("INF")
    else:
        print(distance[i])
