import re


num1, num2 = input().split()


def Rev(string):
    reversed_list = list()
    for i in range(len(string) - 1, -1, -1):
        reversed_list.append(string[i])
    return "".join(reversed_list)


def Add(n1, n2):
    s = int(n1) + int(n2)
    return str(s)


print(int(Rev(Add(Rev(num1), Rev(num2)))))
