import sys
import heapq

n, p, free = map(int, sys.stdin.readline().split())
graph = dict()
for _ in range(p):
    s, e, price = map(int, sys.stdin.readline().split())
    if s in graph.keys():
        graph[s].append((e, price))
    else:
        graph[s] = [(e, price)]
    if e in graph.keys():
        graph[e].append((s, price))
    else:
        graph[e] = [(s, price)]

distance = {node: float("inf") for node in range(1, n + 1)}
distance[1] = 0
parent = dict()
queue = list()
heapq.heappush(queue, [distance[1], 1])
while queue:
    cur_price, cur_n = heapq.heappop(queue)
    if distance[cur_n] < cur_price:
        continue
    if cur_n in graph.keys():
        for next_loc, price in graph[cur_n]:
            next_price = price + cur_price
            if next_price < distance[next_loc]:
                distance[next_loc] = next_price
                heapq.heappush(queue, [distance[next_loc], next_loc])
                if cur_n in parent.keys():
                    parent[cur_n].append(next_loc)
                else:
                    parent[cur_n] = [next_loc]

nodes = list()
costs = list()
heapq.heappush(nodes, [-distance[1], 1])
while nodes:
    price, node = heapq.heappop(nodes)
    if node in distance.keys():
        pass
print(parent)
print(distance)
