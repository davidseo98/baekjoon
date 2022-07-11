from collections import deque
import sys

n_city = int(sys.stdin.readline())
n_bus = int(sys.stdin.readline())
buses = [list(map(int, sys.stdin.readline().split())) for _ in range(n_bus)]
start, destination = map(int, sys.stdin.readline().split())
dp = [[False] * (n_city + 1) for _ in range(n_city + 1)]
link_dict = dict()
for bus in buses:
    if dp[bus[0]][bus[1]]:
        dp[bus[0]][bus[1]] = min(dp[bus[0]][bus[1]], bus[2])
    else:
        dp[bus[0]][bus[1]] = bus[2]

queue = deque()
for i in range(n_city + 1):
    if dp[start][i]:
        queue.append((i, dp[start][i]))
result = list()
while queue:
    cur_station, cur_price = queue.popleft()
    if cur_station == destination:
        result.append(cur_price)
    for i in range(n_city + 1):
        if dp[cur_station][i]:
            queue.append((i, cur_price + dp[cur_station][i]))

print(min(result))
