from collections import deque


def turn_left(deque):
    deque.append(deque.popleft())


def turn_right(deque):
    deque.appendleft(deque.pop())


total_num, want_num = map(int, input().split())
numbers_wanted = deque(map(int, input().split()))
dq = deque(range(1, total_num + 1))
count = 0

while numbers_wanted:
    cur_loc = dq[0]

    if cur_loc == numbers_wanted[0]:
        numbers_wanted.popleft()
        dq.popleft()

    else:
        cur_index = dq.index(cur_loc)
        wanted_index = dq.index(numbers_wanted[0])
        diff_1 = max(cur_index, wanted_index) - min(cur_index, wanted_index)
        diff_2 = min(cur_index, wanted_index) + len(dq) - max(cur_index, wanted_index)
        if cur_index > wanted_index:
            left_diff, right_diff = diff_2, diff_1
        else:
            left_diff, right_diff = diff_1, diff_2

        if left_diff > right_diff:
            _function = turn_right
        else:
            _function = turn_left
        for i in range(min(left_diff, right_diff)):
            _function(dq)
            count += 1


print(count)
