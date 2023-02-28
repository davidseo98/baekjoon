from collections import deque

def bfs(n, graph):
    
    visited = set()
    queue = deque([0])
    visited.add(0)
    
    while queue:
        
        cur = queue.popleft()
        
        for nex in graph[cur]:
            if nex not in visited:
                queue.append(nex)
                visited.add(nex)

    if len(visited) == n: return 1
    else: return 0
    
def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2], reverse = True)
    
    graph = { i : set() for i in range(n)}
    
    for c in costs:
        graph[c[0]].add(c[1])
        graph[c[1]].add(c[0])
        answer += c[2]
    
    for c in costs:

        graph[c[0]].remove(c[1])
        graph[c[1]].remove(c[0])
        
        # 해당 간선을 제거해도 모두 연결되는지 확인
        if not bfs(n, graph):
            graph[c[0]].add(c[1])
            graph[c[1]].add(c[0])
        else:
            answer -= c[2]

    return answer