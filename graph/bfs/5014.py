import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
if S == G:
    print(0)
    exit()
visited = [0] * (F + 1)
queue = deque([S])
visited[S] = 1
answer = 1
# while 1:
while 1:
    if len(queue) == 0:
        print("use the stairs")
        exit()
    next_queue = deque([])
    while queue:
        cur_loc = queue.popleft()
        for loc in [cur_loc + U, cur_loc - D]:
            if 1 <= loc <= F and not (visited[loc]):
                if loc == G:
                    print(answer)
                    exit()
                visited[loc] = 1
                next_queue.append(loc)

    queue = next_queue
    answer += 1
