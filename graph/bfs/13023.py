import sys


def bfs(node):
    stack = list()
    stack.append((node, 1, str(node)))

    while stack:

        cur_node, cur_count, past_nodes = stack.pop()
        if cur_count == 5:
            return 1
        if cur_node in graph.keys():
            for next_node in graph[cur_node]:
                if str(next_node) not in past_nodes:
                    past_nodes += str(next_node)
                    stack.append((next_node, cur_count + 1, past_nodes))
    return 0


n_node, n_edge = map(int, sys.stdin.readline().split())
graph = dict()
for _ in range(n_edge):
    a, b = map(int, sys.stdin.readline().split())
    if a not in graph.keys():
        graph[a] = [b]
    else:
        graph[a].append(b)

    if b not in graph.keys():
        graph[b] = [a]
    else:
        graph[b].append(a)

for i in range(n_node):

    if bfs(i):
        print(1)
        exit()

print(0)
