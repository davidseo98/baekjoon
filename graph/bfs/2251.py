from collections import deque

a, b, c = map(int, input().split())
bottle_list = [a, b, c]
queue = deque()
visited = set()
queue.append((0, 0, c))
visited.add((0, 0, c))
answer = list()
while queue:
    cur = queue.popleft()
    if cur[0] == 0 and cur[2] not in answer and cur[2] > 0:
        answer.append(cur[2])
    for i in range(3):
        for j in range(3):
            next = [-1, -1, -1]
            if i == j or cur[i] == 0 or cur[j] == bottle_list[j]:
                continue
            next[j] = min(bottle_list[j], cur[j] + cur[i])
            next[i] = max(0, cur[i] - (next[j] - cur[j]))
            for m in range(3):
                if next[m] == -1:
                    next[m] = cur[m]
            if tuple(next) not in visited:
                queue.append(tuple(next))
                visited.add(tuple(next))
print(*sorted(answer))
