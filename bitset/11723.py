import sys

n = int(sys.stdin.readline().rstrip())
s = set()
for _ in range(n):
    command = list(sys.stdin.readline().rstrip().split())

    if command[0] == "add":
        if int(command[1]) in s:
            continue
        else:
            s.add(int(command[1]))
    elif command[0] == "remove":
        if int(command[1]) in s:
            s.remove(int(command[1]))
        else:
            continue
    elif command[0] == "check":
        if int(command[1]) in s:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if int(command[1]) in s:
            s.remove(int(command[1]))
        else:
            s.add(int(command[1]))
    elif command[0] == "all":
        s = set(range(1, 21))
    else:
        s = set()
