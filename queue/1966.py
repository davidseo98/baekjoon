from collections import deque


n_case = int(input())
for i in range(n_case):
    n_doc, loc = map(int, input().split())
    queue = deque(map(int, input().split()))
    count = 0
    while 1:
        m = max(queue)
        if loc == 0:
            if queue[0] < m:
                n = queue.popleft()
                queue.append(n)
                loc = len(queue) - 1
            else:
                print(count + 1)
                break
            continue

        if queue[0] < m:
            n = queue.popleft()
            queue.append(n)

        else:
            queue.popleft()
            count += 1
        loc -= 1
