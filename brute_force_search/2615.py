import sys


def check_winner(y, x):
    #print("test for y, x", y, x)
    global graph
    value = graph[y][x]
    is_winner = False
    dx = [0, 1, 1, 1]
    dy = [1, 1, 0, -1]

    for i in range(4):
        #print("which delta", i + 1)
        cnt = 0
        for j in range(1, 6):
            new_x = x + dx[i] * j
            new_y = y + dy[i] * j
            if 0 <= new_x < 19 and 0 <= new_y < 19:
                if graph[new_y][new_x] == value:
                    # print(new_y, new_x)
                    cnt += 1
                else:
                    break
        count_correct = cnt == 4
        past_correct = (
            0 <= x - dx[i] < 19
            and 0 <= y - dy[i] < 19
            and graph[y - dy[i]][x - dx[i]] != value
        ) or (not (0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19))
        next_correct = (
            0 <= new_y < 19 and 0 <= new_x < 19 and graph[new_y][new_x] != value
        ) or (not (0 <= new_y < 19 and 0 <= new_x < 19))

        if count_correct and past_correct and next_correct:
            is_winner = True
            return 1

    if not (is_winner):
        return 0


graph = list()
for _ in range(19):
    graph.append(list(map(int, sys.stdin.readline().split())))

no_winner = True
for i in range(19):
    for j in range(19):
        if graph[i][j] != 0:
            value = graph[i][j]
            #print(i, j)
            if check_winner(i, j):

                no_winner = False
                print(value)
                print(i + 1, j + 1)

if no_winner:
    print(0)
