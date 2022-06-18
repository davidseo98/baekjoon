from collections import deque
import sys


def push(queue, x):
    queue.append(x)


def pop(queue):
    if len(queue) == 0:
        return -1
    else:
        return queue.popleft()


def size(queue):
    return len(queue)


def empty(queue):
    if len(queue) == 0:
        return 1
    else:
        return 0


def front(queue):
    if len(queue) == 0:
        return -1
    else:
        return queue[0]


def back(queue):
    if len(queue) == 0:
        return -1
    else:
        return queue[-1]


command_dict = {
    "push": push,
    "pop": pop,
    "empty": empty,
    "size": size,
    "front": front,
    "back": back,
}

n = int(input())
queue = deque()

for i in range(n):
    input_string = list(sys.stdin.readline().rstrip().split())
    command = command_dict[input_string[0]]
    if command == push:
        push(queue, int(input_string[1]))
    else:
        print(command(queue))
