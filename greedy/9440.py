import sys

while 1:
    num_list = list(sys.stdin.readline().split())
    if num_list[0] == "0":
        break
    n = num_list[0]

    num_list = sorted(num_list[1:], reverse=True)
    zero_count = num_list.count("0")
    num_list = num_list[: len(num_list) - zero_count]
    min1 = num_list.pop()
    min2 = num_list.pop()
    num_list = num_list + ["0"] * zero_count + [min2, min1]
    n1 = list()
    n2 = list()
    while num_list:
        n1.append(num_list.pop())
        if len(num_list) == 0:
            break
        n2.append(num_list.pop())
    print(int("".join(n1)) + int("".join(n2)))
