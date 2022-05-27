import sys

n = int(input())
result = list()


def push():
    result.append(command[1])


def pop():
    if len(result) == 0:
        print(-1)
    else:
        print(result.pop())


def top():
    if len(result) == 0:
        print(-1)
    else:
        print(result[-1])


def size():
    print(len(result))


def empty():
    if len(result) == 0:
        print(1)
    else:
        print(0)


commands_dict = {
    "push": push,
    "pop": pop,
    "top": top,
    "size": size,
    "empty": empty,
}

for i in range(n):
    command = list(sys.stdin.readline().split())
    commands_dict[command[0]]()
