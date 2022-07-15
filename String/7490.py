import sys
from collections import deque


def is_possible(sign):
    global n
    num = list(range(1, n + 1))
    equation = str(num[0])
    original_equation = str(num[0])
    for i in range(n - 1):
        if sign[i] != " ":
            equation += sign[i]
        original_equation += sign[i]
        equation += str(num[i + 1])
        original_equation += str(num[i + 1])
    num_queue = deque()
    sign_queue = deque()
    temp = ""
    for i in range(len(equation)):
        if equation[i] == "+" or equation[i] == "-":
            num_queue.append(int(temp))
            sign_queue.append(equation[i])
            temp = ""
        if i == len(equation) - 1:
            if temp:
                num_queue.append(int(temp + equation[i]))
            else:
                num_queue.append(int(equation[i]))
        if equation[i].isnumeric():
            temp += equation[i]
    while sign_queue:
        sign = sign_queue.popleft()
        num1 = num_queue.popleft()
        num2 = num_queue.popleft()
        if sign == "+":
            num_queue.appendleft(num1 + num2)
        else:
            num_queue.appendleft(num1 - num2)
    if num_queue[0] == 0:
        return original_equation
    else:
        return 0


def dfs():
    global answer
    if len(s) == n - 1:
        result = is_possible(s)
        if result:
            answer.append(result)
        return
    for i in range(3):
        s.append(sign[i])
        dfs()
        s.pop()


t = int(sys.stdin.readline())
sign = ["+", "-", " "]
for _ in range(t):
    answer = list()
    n = int(sys.stdin.readline())
    s = list()
    dfs()
    for a in sorted(answer):
        print(a)
    print()
