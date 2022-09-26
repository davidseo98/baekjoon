import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

num_list.sort()
start = 0
end = n - 1

answer = [float("inf"), -1, -1]
while start != end:
    sum_value = num_list[start] + num_list[end]
    if abs(sum_value) < answer[0]:
        answer[0] = abs(sum_value)
        answer[1] = num_list[start]
        answer[2] = num_list[end]

    else:
        if start + 1 > n - 1:
            end -= 1
            continue
        if end - 1 < 0:
            start += 1
            continue

        can1, can2 = (
            abs(num_list[start + 1] + num_list[end]),
            abs(num_list[start] + num_list[end - 1]),
        )

        if can1 < can2:
            start += 1
        else:
            end -= 1

print(*answer[1:])
