import sys


def is_possible(value):
    global ruby_list, n
    count = 0
    for ruby in ruby_list:
        count += ruby // value
        if ruby % value != 0:
            count += 1
    if count <= n:
        return 1
    else:
        return 0


n, m = map(int, sys.stdin.readline().split())
ruby_list = list()
for _ in range(m):
    ruby_list.append(int(sys.stdin.readline()))

start = 1
answer = start
end = max(ruby_list)
while start <= end:
    mid = (start + end) // 2
    if is_possible(mid) == 1:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
