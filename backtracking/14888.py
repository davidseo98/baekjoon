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


def backtracking():
    global answer, result
    if len(result) == n - 1:
        temp = num_list[0]
        for i in range(1, n):
            temp = calculate(temp, num_list[i], result[i - 1])
        answer.append(temp)
        return

    for i in range(n - 1):
        if visited[i]:
            continue
        result.append(sign_list[i])
        visited[i] = True
        backtracking()
        result.pop()
        visited[i] = False


n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
sign_temp = list(map(int, sys.stdin.readline().split()))
sign_list = list()
visited = [False] * (n - 1)
for i in range(4):
    sign_list += [i] * sign_temp[i]
answer = list()
result = list()
backtracking()
print(max(answer))
print(min(answer))
