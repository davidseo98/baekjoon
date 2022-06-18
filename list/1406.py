import sys
from collections import deque


def L(front: list, back: list) -> None:
    if len(front) == 0:
        return
    else:
        back.appendleft(front.pop())


def D(front: int, back: int) -> None:
    if len(back) == 0:
        return
    else:
        front.append(back.popleft())


def B(front: list) -> None:
    if len(front) == 0:
        return
    else:
        front.pop()


def P(front: list, value: str) -> None:
    front.append(value)


commands_dict = {"L": L, "D": D, "B": B, "P": P}

init_string = sys.stdin.readline().rstrip()
front_list = list()
back_list = deque()

for i in range(len(init_string)):
    front_list.append(init_string[i])

n = int(sys.stdin.readline())

for i in range(n):
    command = list(sys.stdin.readline().rstrip().split())
    c = commands_dict[command[0]]
    if c == P:
        P(front_list, command[1])
    elif c == D:
        D(front_list, back_list)
    elif c == B:
        B(front_list)
    elif c == L:
        L(front_list, back_list)

print("".join(front_list) + "".join(list(back_list)))
