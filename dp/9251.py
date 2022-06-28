import sys

string1 = " " + sys.stdin.readline().rstrip()
string2 = " " + sys.stdin.readline().rstrip()

counts = [[0] * (len(string1)) for _ in range(len(string2))]

for i in range(1, len(string2)):
    cur_letter = string2[i]
    for j in range(1, len(string1)):
        if cur_letter == string1[j]:
            counts[i][j] = counts[i - 1][j - 1] + 1
        else:
            counts[i][j] = max(counts[i][j - 1], counts[i - 1][j])
print(counts[-1][-1])
