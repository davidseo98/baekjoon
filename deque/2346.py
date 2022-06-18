from collections import deque
import sys


def move_left(deque: deque) -> None:
    deque.appendleft(deque.pop())


def move_right(deque: deque) -> None:
    deque.append(deque.popleft())


n = int(input())
dq = deque(map(int, sys.stdin.readline().rstrip().split()))
num_dq = deque(range(1, n + 1))
result = list()

while dq:

    num = dq.popleft()
    result.append(num_dq.popleft())
    _function = move_left if num < 0 else move_right
    if num > 0:
        num -= 1
    if len(dq) == 1:
        result.append(num_dq.pop())
        for num in result:
            print(num, end=" ")
        exit()
    for _ in range(abs(num)):
        _function(dq)
        _function(num_dq)
