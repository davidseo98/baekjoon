from collections import deque

s = input()
t = input()

queue = deque([t])
visited = set()
while queue:
    cur = queue.popleft()
    if len(cur) > 0:
        if cur == s:
            print(1)
            exit()
        if cur[0] == "B":
            if cur[-1] == "A":
                queue.append(cur[: len(cur) - 1])
            queue.append(cur[::-1][: len(cur) - 1])
        else:
            if cur[-1] == "A":
                queue.append(cur[: len(cur) - 1])
print(0)
