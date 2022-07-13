import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
cnt = 0
temp = 0
is_pos = False
for i in range(1, n + 1):
    temp += i
    cnt += 1
    if temp >= k:
        temp -= i
        is_pos = True
        break

for i in range(n, 0, -1):
    if is_pos:
        break
    cnt += 1
    temp += i
    if temp >= k:
        temp -= i
        break
loc_diff = k - temp
cur_line = cnt + 1
diff = cur_line - n
rest = n
candidate = list()
while diff <= n:
    num = rest * diff
    if num > 0:
        candidate.append((rest * diff))
    rest -= 1
    diff += 1
candidate.sort()

print(candidate[loc_diff])
