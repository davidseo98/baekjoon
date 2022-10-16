import sys

n_ladder, n_snake = map(int, sys.stdin.readline().split())
ladders_start = list()
ladders_end = list()
snakes = list()

for _ in range(n_ladder):
    start, end = map(int, sys.stdin.readline().split())
    ladders_start.append(start)
    ladders_end.append(end)

for _ in range(n_snake):
    start, end = map(int, sys.stdin.readline().split())
    snakes.append(start)

start = 1
answer = 0

while start != 100:
    
    answer += 1
    possible_ladders = list()
    possible_blocks = list()
    for c in [start + x for x in range(1, 7)]:
        if c == 100:
            possible_blocks.append(100)
            break
        for i in range(n_ladder):
            if ladders_start[i] == c:
                possible_ladders.append((c, ladders_end[i]))
                # 동일 시작 위치의 사다리가 여러 개 있을 수도 있으니 일단 no break

        if c in snakes:
            continue
        else:
            possible_blocks.append(c)

    if possible_ladders and 100 not in possible_blocks:
        possible_ladders.sort(key=lambda x: x[1])
        start = possible_ladders[-1][1]
    else:
        start = max(possible_blocks)

    

print(answer)
