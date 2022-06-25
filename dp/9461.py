import sys

def fan(num) :
    global memo
    length = len(memo)
    if num >= length :
        for i in range(length, num) :
            memo.append(memo[i - 1] + memo[i - 5])
    print(memo[num-1])

n = int(sys.stdin.readline())
for _ in range(n) :
    memo = [1, 1, 1, 2, 2]
    fan(int(sys.stdin.readline()))