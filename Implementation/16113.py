import sys

n = int(sys.stdin.readline())
string = sys.stdin.readline().strip()
elements = [[] for _ in range(n // 5)]
answer = ""
for i in range(n):
    loc = i % (n // 5)
    val = 1 if string[i] == "#" else 0
    elements[loc].append(val)
if n == 5:
    if sum(elements[0]) == 5:
        print(1)
        exit()
finish = n // 5
loc = 0
while loc < finish:
    if sum(elements[loc]) == 0:
        loc += 1
        continue
    if sum(elements[loc]) == 5 and (loc == finish - 1 or sum(elements[loc + 1]) == 0):
        answer += "1"
        loc += 1
        continue
    n1, n2, n3 = sum(elements[loc]), sum(elements[loc + 1]), sum(elements[loc + 2])
    if n1 == 5 and n2 == 2 and n3 == 5:
        answer += "0"
    elif n1 == 3 and n2 == 3 and n3 == 5:
        answer += "3"
    elif n1 == 3 and n2 == 1 and n3 == 5:
        answer += "4"
    elif n1 == 5 and n2 == 3 and n3 == 4:
        answer += "6"
    elif n1 == 1 and n2 == 1 and n3 == 5:
        answer += "7"
    elif n1 == 5 and n2 == 3 and n3 == 5:
        answer += "8"
    elif n1 == 4 and n2 == 3 and n3 == 5:
        answer += "9"
    else:
        if elements[loc][1] == 0:
            answer += "2"
        else:
            answer += "5"
    loc += 3

print(answer)
