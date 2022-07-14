import sys


def is_possible(ruby, mid):
    global bag_list
    if ruby <= bag_list[mid]:
        return 1
    return 0


n, k = map(int, sys.stdin.readline().split())
ruby_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bag_list = [int(sys.stdin.readline()) for _ in range(k)]

ruby_list.sort()
ruby_list.sort(key=lambda x: x[1], reverse=True)
bag_list.sort()
print(ruby_list)
answer = 0
for ruby in ruby_list:
    if len(bag_list) == 0:
        break
    if ruby[0] > bag_list[-1]:
        continue
    else:
        result = 0
        lo = 0
        hi = len(bag_list) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if is_possible(ruby[0], mid):
                result = mid
                hi = mid - 1
            else:
                lo = mid + 1
        print(bag_list[mid], ruby[1])
        bag_list.pop(mid)
        answer += ruby[1]

print(answer)
