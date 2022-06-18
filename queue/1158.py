n, loc = map(int, input().split())
loc -= 1
dist = loc
queue = list(range(1, n + 1))
result = list()
while queue:
    result.append(str(queue.pop(loc)))
    if len(queue) == 0:
        break
    loc = (loc + dist) % len(queue)

print("<" + ", ".join(result) + ">")
