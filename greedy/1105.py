import sys

start, finish = sys.stdin.readline().split()
if len(start) < len(finish):
    print(0)
    exit()
cnt = 0
for i in range(len(start)):
    if start[i] == "8" and finish[i] == "8":
        cnt += 1
    if start[i] != finish[i]:
        break
print(cnt)
