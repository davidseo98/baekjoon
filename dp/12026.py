import sys

n = int(sys.stdin.readline())
road = sys.stdin.readline().strip()
dp = [n * n] * n
visited = [False] * n
dp[0] = 0
visited[0] = True
boj = {"B": "J", "O": "B", "J": "O"}
for i in range(1, n):
    past_letter = boj[road[i]]
    for j in range(0, i):
        if road[j] == past_letter and visited[j]:
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
            visited[i] = True
# print(dp)
# print(visited)
if not visited[n - 1]:
    print(-1)
else:
    print(dp[n - 1])
