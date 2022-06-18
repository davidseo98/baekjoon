from collections import deque

n_case = int(input())


def delete(deque: deque, is_reverse: bool) -> deque:
    if is_reverse:
        deque.pop()
    else:
        deque.popleft()


def preprocess(string: str) -> list:
    if len(string) == 2:
        return deque()
    else:
        return deque(string[1:-1].split(","))


for i in range(n_case):
    is_reverse = False
    commands = input()
    n = int(input())
    dq = preprocess(input())
    is_error = 0
    for command in commands:
        if command == "R":
            is_reverse = not (is_reverse)
        else:
            if len(dq) == 0:
                print("error")
                is_error = 1
                break
            else:
                delete(dq, is_reverse)
    if is_error:
        continue
    else:
        if is_reverse:
            print("[" + ",".join(list(dq)[::-1]) + "]")
        else:
            print("[" + ",".join(dq) + "]")
