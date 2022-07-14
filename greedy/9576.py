import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    book_list = list(range(1, n + 1))
    request_list = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    request_count = [0] * (n + 1)
    for i in range(m):
        request = request_list[i]
        request_list[i].append(request[1] - request[0])
        for i in range(request[0], request[1] + 1):
            request_count[i] += 1
    request_list.sort(key=lambda x: x[2])
    for request in request_list:
        min_request = [1001, -1]
        for i in range(request[0], request[1] + 1):
            if min_request[0] > request_count[i] and i in book_list:
                min_request[0] = request_count[i]
                min_request[1] = i
        if min_request[1] == -1:
            continue
        else:
            book_list.remove(min_request[1])
            request_count[min_request[1]] = max(0, request_count[min_request[1]] - 1)
    print(n - len(book_list))
