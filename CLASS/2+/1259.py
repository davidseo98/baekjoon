import sys

n = sys.stdin.readline().rstrip()
while n != "0":
    correct = 1
    for i in range(len(n) // 2):
        if n[i] != n[(len(n) - 1) - i]:
            correct = 0
            break
    if correct:
        print("yes")
    else:
        print("no")

    n = sys.stdin.readline().rstrip()
