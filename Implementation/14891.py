import sys
from collections import deque


def counter_clockwise(queue):
    temp = queue.popleft()
    queue.append(temp)


def clockwise(queue):
    temp = queue.pop()
    queue.appendleft(temp)


gears_list = list()
for _ in range(4):
    gears_list.append(deque(map(int, sys.stdin.readline().rstrip())))

n = int(sys.stdin.readline())
for _ in range(n):
    gear_num, direction = map(int, sys.stdin.readline().split())
    gear_num -= 1
    instructions = dict()
    instructions[gear_num] = direction

    for next in range(gear_num + 1, 4):
        if gears_list[next - 1][2] != gears_list[next][6]:
            instructions[next] = -(instructions[next - 1])
        else:
            break

    for past in range(gear_num - 1, -1, -1):
        if gears_list[past + 1][6] != gears_list[past][2]:
            instructions[past] = -(instructions[past + 1])
        else:
            break

    for gear, dir in instructions.items():
        if dir == 1:
            clockwise(gears_list[gear])
        else:
            counter_clockwise(gears_list[gear])

answer = 0
for i in range(4):
    if gears_list[i][0]:
        answer += 2 ** (i)


print(answer)
