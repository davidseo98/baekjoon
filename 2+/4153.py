import sys

num_list = list(map(int, sys.stdin.readline().split()))
while sum(num_list) != 0:
    num_list.sort()
    if num_list[0] ** 2 + num_list[1] ** 2 == num_list[2] ** 2:
        print("right")
    else:
        print("wrong")
    num_list = list(map(int, sys.stdin.readline().split()))
