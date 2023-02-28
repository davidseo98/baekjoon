from collections import defaultdict

s = []
answer = []
def dfs(cur, tickets, visited):
    global s, answer
    
    if len(s) == len(tickets) and len(answer) == 0:
        answer = s[:]
        return
    
    for i in range(len(tickets)):
        if i not in visited and tickets[i][0] == cur:
            visited.add(i)
            s.append(tickets[i][1])
            dfs(tickets[i][1], tickets, visited)
            visited.remove(i)
            s.pop()
    
def solution(tickets):
    global answer
    tickets.sort(key = lambda x : x[1])
    visited = set()
    dfs('ICN', tickets, visited)
    
    return ['ICN'] + answer