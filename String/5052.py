import sys
import heapq

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    phone_list = list()
    for _ in range(n):
        num = sys.stdin.readline().strip()
        heapq.heappush(phone_list, (len(num), num))
    is_possible = True
    while phone_list:
        cur_num = heapq.heappop(phone_list)
        for i in range(len(phone_list)):
            if phone_list[i][0] == cur_num[0]:
                print(phone_list[i], cur_num)
                continue
            if cur_num[1] == phone_list[i][1][: len(cur_num[1])]:
                print("NO")
                is_possible = False
                break
        if not is_possible:
            break
    if is_possible:
        print("YES")
