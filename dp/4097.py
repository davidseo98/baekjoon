import sys

n = int(sys.stdin.readline())
while n != 0:
    price_list = list()
    for _ in range(n):
        price_list.append(int(sys.stdin.readline()))
    for i in range(1, n):
        price_list[i] = max(price_list[i], price_list[i - 1] + price_list[i])
    print(max(price_list))

    n = int(sys.stdin.readline())
