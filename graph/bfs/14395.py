import sys
from collections import deque
from math import sqrt

start, end = map(int, sys.stdin.readline().split())
limit = int(1e9)
visited = [False] * limit
queue = deque()
queue.append(start)
visited[start] = True
answer = list()
while queue :
    cur = queue.popleft()
    if cur == end :
        result = ""
        while cur != start :
            if visited[cur] == "+" :
                cur = cur // 2
                result += "+"
            elif visited[cur] == "*" :
                cur = int(sqrt(cur))
                result += "*"
            else :
                cur = visited[cur]
                result += "/"
        answer.append(result[::-1])

    if 0 <= cur + cur <= limit and not visited[cur + cur]: 
        queue.append(cur + cur)
        visited[cur + cur] = "+"
    if 0 <= cur * cur <= limit and not visited[cur * cur]:
        queue.append(cur * cur)
        visited[cur * cur] = "*"
    if cur != 0 and not visited[1]:
        queue.append(1)
        visited[1] = cur 

if len(answer) == 0 :
    print(-1)
else :
    print(sorted(answer)[0])
            
