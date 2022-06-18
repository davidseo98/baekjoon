from collections import deque
import sys


def push_front(deque, x):
    deque.appendleft(x)


def push_back(deque, x):
    deque.append(x)


def pop_front(deque):
    if len(deque) == 0:
        return -1
    else:
        return deque.popleft()


def pop_back(deque):
    if len(deque) == 0:
        return -1
    else:
        return deque.pop()


def size(deque):
    return len(deque)


def empty(deque):
    if len(deque) == 0:
        return 1
    else:
        return 0


def front(deque):
    if len(deque) == 0:
        return -1
    else:
        return deque[0]


def back(deque):
    if len(deque) == 0:
        return -1
    else:
        return deque[-1]


command_dict = {
    "push_front": push_front,
    "push_back": push_back,
    "pop_front": pop_front,
    "pop_back": pop_back,
    "size": size,
    "empty": empty,
    "front": front,
    "back": back,
}

dq = deque()
n = int(input())
for i in range(n):
    input_string = list(sys.stdin.readline().rstrip().split())
    command = command_dict[input_string[0]]
    if command == push_back or command == push_front:
        command(dq, int(input_string[1]))
    else:
        print(command(dq))
