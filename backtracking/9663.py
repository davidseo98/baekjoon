import sys
sys.setrecursionlimit(50000)

n = int(sys.stdin.readline())
answer = 0
unable = [[0]*n for _ in range(n)]
x_unable = []
y_unable = []

def check_unable(x, y):
    for i in range(len(x_unable)):
        if x == x_unable[i] or y == y_unable[i] or abs(x - x_unable[i]) == abs(y - y_unable[i]):
            return 0
    return 1


def dfs(count):
    global unable, answer

    if count == n:
        answer += 1
        return 

    for i in range(n):
        for j in range(n):
            if check_unable(i, j):
                x_unable.append(i)
                y_unable.append(j)
                dfs(count + 1)
                x_unable.pop()
                y_unable.pop()

dfs(0)
print(answer)