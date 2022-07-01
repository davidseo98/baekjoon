import sys
from collections import deque

me, you = map(int, sys.stdin.readline().split())
if me == you:
    print(0)
    exit()
visited = [0] * 100001
cur_queue = deque([me])
visited[me] = 1
answer = 1
while 1:
    next_queue = deque([])
    while cur_queue:
        cur_loc = cur_queue.popleft()
        for loc in [cur_loc - 1, cur_loc + 1, cur_loc * 2]:
            if 0 <= loc <= 100000 and not (visited[loc]):
                if loc == you:
                    print(answer)
                    exit()
                visited[loc] = 1
                next_queue.append(loc)
    answer += 1
    cur_queue = next_queue
