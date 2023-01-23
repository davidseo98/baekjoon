# 구분 : brute-force
# 소요시간 : 대략 10분

from collections import deque, defaultdict

def bfs(graph, start, visited):
    queue = deque([])
    queue.append(start)
    visited[start] = True
    cnt = 1
    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                cnt += 1
    return cnt

def solution(n, wires):
    graph = defaultdict(list)
    diff = 10000
    # initialize graph
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    
    # brute-force algorithm
    for wire in wires:
        visited = [False] * (n + 1)
        
        graph[wire[0]].remove(wire[1])  # remove one wire
        graph[wire[1]].remove(wire[0])
        
        result = []
        for node in range(1, n + 1):    # check sizes
            if visited[node]: continue
            result.append(bfs(graph, node, visited))
            
        graph[wire[0]].append(wire[1])  # recover graph
        graph[wire[1]].append(wire[0])
        
        new_diff = abs(result[0] - result[1])
        if new_diff < diff: diff = new_diff
        
    return diff