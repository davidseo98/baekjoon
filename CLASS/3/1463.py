n = int(input())
three_count = 0
best = 100
while 3**three_count <= n:
    num = n
    cnt = 0
    left_over = list()
    for _ in range(three_count):
        left_over.append(num % 3)
        num = num // 3
        cnt += 1

    while num != 1:
        left_over.append(num % 2)
        num = num // 2
        cnt += 1
    answer = cnt + sum(left_over)

    if answer < best:
        best = answer

    three_count += 1

print(best)
