import sys
input = sys.stdin.readline

a_n, b_n = map(int, input().split())
num_a = list(map(int, input().split()))
num_b = list(map(int, input().split()))

result_list = list()
a, b = 0, 0

while True:

    if a == a_n and b == b_n: break

    if a == a_n: 
        result_list.append(num_b[b])
        b += 1

    elif b == b_n:
        result_list.append(num_a[a])
        a += 1

    elif num_a[a] <= num_b[b]:
        result_list.append(num_a[a])
        a += 1

    elif num_a[a] > num_b[b]: 
        result_list.append(num_b[b])
        b += 1

print(*sorted(result_list))

