import sys

sys.setrecursionlimit(10000)


def dfs(length):
    global num, new_channel, diff, switch
    if switch or length == 0:
        return

    if len(num) == length:
        number = int("".join(map(str, num)))
        new_diff = abs(int(target) - number)
        if new_diff < diff:
            new_channel = number
            diff = new_diff
        return

    for i in candidate:
        num.append(i)
        dfs(length)
        num.pop()


target = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
broken = list(map(int, sys.stdin.readline().rstrip().split()))

candidate = sorted([x for x in range(0, 10) if x not in broken])
length = len(target)
diff = float("inf")
new_channel = "hey"
num = list()
switch = False

dfs(length - 1)
dfs(length)
dfs(length + 1)

if new_channel == "hey":
    print(abs(100 - int(target)))
else:
    print(
        min(
            len(str(new_channel)) + abs(int(target) - new_channel),
            abs(100 - int(target)),
        )
    )
