from collections import deque


def normal_end():
    global result
    for i in result:
        print(i)
    exit()


def error():
    print("NO")
    exit()


def check_if_end():
    global num_stack, numbers
    if len(num_stack) == 0 and len(numbers) == 0:
        normal_end()


n = int(input())
numbers = list(range(n, 0, -1))
num_stack = list()
cur_num = 0
seq_stack = deque()
result = list()

for i in range(n):
    seq_stack.appendleft(int(input()))

num_stack.append(numbers.pop())
result.append("+")
cur_num = num_stack[-1]
while 1:

    cur_seq_num = seq_stack.pop()
    while cur_num < cur_seq_num:
        num_stack.append(numbers.pop())
        result.append("+")
        cur_num = num_stack[-1]

    if cur_num == cur_seq_num:

        num_stack.pop()
        result.append("-")

        if len(num_stack) == 0:
            try:
                num_stack.append(numbers.pop())
                result.append("+")
            except:
                check_if_end()
                continue

        cur_num = num_stack[-1]

    elif cur_num > cur_seq_num:
        error()
