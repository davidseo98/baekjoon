import sys

n = int(sys.stdin.readline())
time_table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
time_table.sort(key=lambda x: x[0])
time_table.sort(key=lambda x: x[1])
end = 0
count = 0
for time in time_table:
    if time[0] >= end:
        count += 1
        end = time[1]

print(count)
