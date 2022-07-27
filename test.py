import sys

n = int(sys.stdin.readline())
answer = 0
for i in range(1, n + 1):
    string = str(i)
    if len(string) < 3:
        answer += 1
        continue
    p_d = int(string[1]) - int(string[0])
    is_not = False
    for j in range(len(string) - 1):
        d = int(string[j + 1]) - int(string[j])
        if p_d != d:
            is_not = True
            break
    if not is_not:
        answer += 1
        p_d = d
print(answer)