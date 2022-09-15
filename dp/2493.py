import sys

n = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))
answer = [0] * n
memo = [(towers[-1], n - 1)]
for i in range(n - 2, -1, -1):

    cur_tower = towers[i]
    if cur_tower < memo[-1][0]:
        memo.append((cur_tower, i))

    else:
        while memo and cur_tower >= memo[-1][0]:
            _, loc = memo.pop()
            answer[loc] = i + 1
        memo.append((cur_tower, i))

print(*answer)
