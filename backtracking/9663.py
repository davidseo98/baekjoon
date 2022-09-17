import sys


def check_places(x, y):
    global visited
    for i in range(n):
        visited[i][y] += 1
        visited[x][i] += 1

    pass


def uncheck_places(x, y):
    global visited

    pass


def dfs():
    global answer, queens

    if len(queens) == n:
        is_possible = True
        for m in range(n):
            for k in range(m + 1, n):

                x1, y1 = queens[m]
                x2, y2 = queens[k]

                if x1 == x2 or y1 == y2 or abs(x1 - x2) / abs(y1 - y2) == 1.0:
                    is_possible = False

        if is_possible:
            answer += 1

        return

    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            queens.append((i, j))
            visited[i][j] = True
            dfs()
            queens.pop()
            visited[i][j] = False


n = int(sys.stdin.readline())
visited = [[False] * n for _ in range(n)]
queens = list()
answer = 0

dfs()

print(answer)
