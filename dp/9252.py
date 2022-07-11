import sys

string1 = " " + sys.stdin.readline().rstrip()
string2 = " " + sys.stdin.readline().rstrip()

counts = [[0] * (len(string1)) for _ in range(len(string2))]
dp = dict()

for i in range(1, len(string2)):
    cur_letter = string2[i]
    for j in range(1, len(string1)):
        if cur_letter == string1[j]:
            counts[i][j] = counts[i - 1][j - 1] + 1
            dp[(i, j)] = (i - 1, j - 1)
        else:
            if counts[i][j - 1] > counts[i - 1][j]:
                counts[i][j] = counts[i][j - 1]
                dp[(i, j)] = (i, j - 1)
            else:
                dp[(i, j)] = (i - 1, j)
                counts[i][j] = counts[i - 1][j]
max_count = counts[-1][-1]

is_break = False
for i in range(len(string2)):
    for j in range(len(string1)):
        if counts[i][j] == max_count:
            start_x, start_y = j, i
            is_break = True
        if is_break:
            break
    if is_break:
        break

lcs = []
prev_val = max_count
while 1:
    cur_val = counts[start_y][start_x]
    if cur_val < prev_val:
        lcs.append(string2[prev_y])
    if (start_y, start_x) not in dp.keys():
        break
    prev_x, prev_y = start_x, start_y
    start_y, start_x = dp[(start_y, start_x)]
    prev_val = cur_val
print(counts[-1][-1])
print("".join(lcs[::-1]))
