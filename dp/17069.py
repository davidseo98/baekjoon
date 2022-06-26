import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
state = [[0] * n for _ in range(n)]
state[0][1] = "0"
dp[0][1] = 1
check_dict = {
    "0": [[0], [0, 1, 2], "0"],
    "45": [[0], [0, 1, 2], [2]],
    "90": ["0", [0, 1, 2], [2]],
}
move_list = [(1, 0), (1, 1), (0, 1)]
# bottom up method
for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            continue
        # print(i, j)
        cur_state = state[i][j]
        # print(cur_state)
        check = []
        for dx, dy in move_list:
            new_x, new_y = j + dx, i + dy
            if 0 <= new_x < n and 0 <= new_y < n:
                if graph[new_y][new_x] == 0:
                    check.append(True)
                    continue
            check.append(False)
        # print("check list",check)
        for c in range(len(check_dict[cur_state])):

            if check_dict[cur_state][c] == "0":
                # print("skipped")
                continue
            # print(check_dict[cur_state][c])
            # print("je")
            is_poss = True
            for loc in check_dict[cur_state][c]:
                print(loc)
                print(check[loc])
                if not (check[loc]):
                    is_poss = False
                    break
            if is_poss:
                dx, dy = move_list[c]
                new_x, new_y = j + dx, i + dy
                print(new_x, new_y)
                if 0 <= new_x < n and 0 <= new_y < n:
                    # print("hey")
                    dp[new_y][new_x] += dp[i][j]
                    state[new_y][new_x] = list(check_dict.keys())[c]
                    print("e")
                    # print(dp)
                    for line in state:
                        print(line)
                    print("----------")
                    for line in dp:
                        print(line)

for line in graph:
    print(line)
print("----------")
for line in dp:
    print(line)
print(dp[-1][-1])
