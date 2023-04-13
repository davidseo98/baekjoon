import sys, heapq

input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
    num, start, end = map(int, input().split())
    heapq.heappush(classes, (start, end, num))

answer = 0
cur_classes = []
class2room = dict()
using_room = set()
available_room = []
temp = []

while classes:

    s, e, num = heapq.heappop(classes)

    while cur_classes and cur_classes[0][0] <= s:
        _, end_num = heapq.heappop(cur_classes)
        using_room.remove(class2room[end_num])
        available_room.append(class2room[end_num])
    
    heapq.heappush(cur_classes, (e, num))

    if answer < len(cur_classes):
        answer = len(cur_classes)
        class2room[num] = answer
        using_room.add(answer)
    else:
        class2room[num] = available_room.pop()
        using_room.add(class2room[num])


print(answer)
for _class in range(1, n + 1):
    print(class2room[_class])
