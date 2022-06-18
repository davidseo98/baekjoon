import sys
from collections import deque


def left_shift(front: list, back: deque):
    if len(front) == 0:
        return
    else:
        back.appendleft(front.pop())


def right_shift(front: list, back: deque):
    if len(back) == 0:
        return
    else:
        front.append(back.popleft())


def delete(front: list):
    if len(front) == 0:
        return
    else:
        front.pop()


n = int(input())
for i in range(n):
    front_list = list()
    back_dq = deque()

    input_string = sys.stdin.readline().rstrip()
    for j in range(len(input_string)):

        char = input_string[j]
        if char.isalnum():
            front_list.append(char)
        elif char == "<":
            left_shift(front_list, back_dq)
        elif char == ">":
            right_shift(front_list, back_dq)
        elif char == "-":
            delete(front_list)

    print("".join(front_list) + "".join(list(back_dq)))
