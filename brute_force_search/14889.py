import sys
from itertools import combinations

def cal_diff(s):
    team1, team2 = s, [x for x in total if x not in s]
    scores = [0, 0]
    for idx, team in enumerate([team1, team2]):
        for c in list(combinations(team, 2)):
            i, j = c
            scores[idx] += (matrix[i][j] + matrix[j][i])
    print(scores)
    return abs(scores[0] - scores[1])

def dfs(loc):
    global s, answer

    if len(s) == n // 2:
        diff = cal_diff(s)
        if diff < answer: answer = diff
        return 

    for i in range(loc, n):
        s.append(i)
        dfs(i + 1)
        s.pop()

    
answer = float("inf")
s = []
n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
total = list(range(n))

dfs(0)

print(answer)