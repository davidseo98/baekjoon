import sys

n = int(sys.stdin.readline())
for _ in range(n): 
    string = sys.stdin.readline().strip()
    loc = 0
    while loc < len(string) :
        if string[loc] == "0" :
            