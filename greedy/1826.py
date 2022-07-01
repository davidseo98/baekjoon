import sys

n = int(sys.stdin.readline())
stations = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
destination, cur_fuel = map(int, sys.stdin.readline().split())
cur_loc = 0
answer = 0
while 1:
    cur_loc += cur_fuel
    if cur_loc >= destination:
        break
    possible_stations = [x for x in stations if x[0] <= cur_loc]
    if len(possible_stations) == 0:
        print(-1)
        exit()
    possible_stations.sort(key=lambda x: x[1])
    visited_station = possible_stations[-1]
    stations.remove(visited_station)
    charged_fuel = visited_station[1]
    cur_fuel = charged_fuel
    answer += 1

print(answer)
