from collections import deque

def get_neighbor(cur, words):
    neighbors = []
    
    for w in words:
        if len(w) != len(cur): continue
        diff_cnt = 0
        for idx in range(len(w)):
            if w[idx] != cur[idx]: diff_cnt += 1
        
        if diff_cnt == 1: neighbors.append(w)
    
    return neighbors

def bfs(begin, target, words):
    queue = deque([(begin, 0, begin + '.')])
    
    while queue:
        cur, cnt, visited = queue.popleft()
        if cur == target: return cnt
    
        for n in get_neighbor(cur, words):
            if n not in visited:
                queue.append((n, cnt + 1, visited + n + "."))
    return 0

def solution(begin, target, words):

    return bfs(begin, target, words)