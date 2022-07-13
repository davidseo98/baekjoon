import sys


def calculate(cur_num, next_num, sign_num):
    if sign_num == 0:
        return cur_num + next_num
    elif sign_num == 1:
        return cur_num - next_num
    elif sign_num == 2:
        return cur_num * next_num
    else:
        if cur_num < 0:
            return -(-cur_num // next_num)
        return cur_num // next_num


def dfs(depth, total, plus, minus, multiply, divide):
    global answer
    if depth == n:
        answer.append(total)
        return

    if plus:
        dfs(depth + 1, total + num_list[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num_list[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num_list[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num_list[depth]), plus, minus, multiply, divide - 1)


n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
sign_list = list(map(int, sys.stdin.readline().split()))
visited = [False] * (n - 1)
answer = list()
dfs(1, num_list[0], sign_list[0], sign_list[1], sign_list[2], sign_list[3])
print(max(answer))
print(min(answer))
