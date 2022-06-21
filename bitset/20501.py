import sys

n = int(sys.stdin.readline().rstrip())
friends_info = list()
for _ in range(n):
    friends_info.append(sys.stdin.readline().rstrip())

q = int(sys.stdin.readline().rstrip())
for _ in range(q):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    a_f, b_f = int(friends_info[a - 1], 2), int(friends_info[b - 1], 2)
    print(bin(int(bin(a_f & b_f)[2:], 2)).count("1"))
    # print(a_f)
    # for i in range(len(a_f)):
    #    if int(a_f[i]) and int(b_f[i]):
    #        cnt += 1
    # print(cnt)
