from collections import defaultdict, deque

def bfs(graph, info):
    answer = 1
    queue = deque([(0, 1, 1, "/0/", "/0/")])
    
    while queue:
        cur, diff, sheep_cnt, candidate, visited = queue.popleft()
        answer = max(answer, sheep_cnt)
        
        # 현재 노드의 자식을 candidate(갈 수 있는 곳)에 추가 
        for child in graph[int(cur)]:
            candidate += (str(child) + "/")
        
        for child in candidate.split("/"):
            
            # 만약 이 path에서 이미 간 노드라면 continue
            if child == "" or "/" + child + "/" in visited: continue
            new_visited = visited + str(child) + "/"
            
            # 늑대를 더 허용할 수 있는 경우
            if diff >= 2:   
                if info[int(child)]:
                    queue.append((child, diff - 1, sheep_cnt, candidate, new_visited))
                else:
                    queue.append((child, diff + 1, sheep_cnt + 1, candidate, new_visited))
            # 늑대를 더 허용할 수 없는 경우
            else:
                if info[int(child)] == 0:
                    queue.append((child, diff + 1, sheep_cnt + 1, candidate, new_visited))
    return answer
    
def solution(info, edges):
    
    # 주어진 간선 정보로 그래프 생성
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
    
    return bfs(graph, info)