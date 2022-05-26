n, m = map(int, input().split())

cnt = 1
for i in range(n) :
    for j in range(m) :
        if (j+1) == m :
            print(cnt, end = "\n")
        else :
            print(cnt, end = " ")
        cnt +=1