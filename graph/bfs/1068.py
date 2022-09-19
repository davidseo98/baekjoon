import sys
from collections import deque


def remove_node(d):
    global graph
    parent = num_list[d]
    if parent == -1:
        print(0)
        exit()
    graph[parent].remove(d)
    if len(graph[parent]) == 0:
        del graph[parent]


def bfs():
    global answer
    queue = deque()
    queue.append(-1)
    while queue:
        c_node = queue.popleft()
        if c_node in graph.keys():
            for n_node in graph[c_node]:
                queue.append(n_node)
        else:
            answer += 1


n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
delete = int(sys.stdin.readline())
graph = dict()
for i in range(n):
    if num_list[i] in graph.keys():
        graph[num_list[i]].append(i)
    else:
        graph[num_list[i]] = [i]
answer = 0

remove_node(delete)
bfs()

# print(graph)
print(answer)
