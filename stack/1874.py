n = int(input())
numbers = list()
stack = []
use_numbers = list(range(10, 1, -1))
result = list()
moves = []


def add():
    try:
        stack.append(use_numbers.pop())
        moves.append("+")
    except:
        if result != numbers:
            print("NO")
            exit()


for i in range(n):
    numbers.append(int(input()))

for number in numbers:
    if len(stack) == 0:
        add()

    if stack[-1] < number:
        while stack[-1] < number:
            add()
        result.append(stack.pop())
        moves.append("-")
    elif stack[-1] > number:
        cur_num = result.pop()
        if cur_num != number:
            print("NO")
            exit()
        moves.append("-")
    else:
        result.append(stack.pop())
        moves.append("-")

for m in moves:
    print(m)
