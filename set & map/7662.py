import sys
from heapq import *


def I(value: int) -> None:
    global min_heap, max_heap, insert_count
    heappush(min_heap, value)
    heappush(max_heap, -value)
    insert_count += 1


def D(value: int) -> None:
    global min_heap, max_heap, delete_count, insert_count
    if delete_count == insert_count:
        print("ignored", insert_count, delete_count)
        return
    if value < 0:
        heappop(min_heap)
    elif value > 0:
        heappop(max_heap)
    delete_count += 1


command_dict = {"I": I, "D": D}
delete_count, insert_count = 0, 0
test_num = int(sys.stdin.readline().rstrip())

for i in range(test_num):
    min_heap, max_heap = list(), list()
    command_num = int(sys.stdin.readline().rstrip())

    for j in range(command_num):
        command = list(sys.stdin.readline().rstrip().split())
        c = command_dict[command[0]]
        c(int(command[1]))

    if delete_count == insert_count:
        print("EMPTY")
    else:
        print(-max_heap[0], min_heap[0])
