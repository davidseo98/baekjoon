n = int(input())
result = [[] for _ in range(n)]
for i in range(n) :
    c = int(input())
    for j in range(4) :
        result[i].append(c//25)
        c=c%25
        result[i].append(c//10)
        c=c%10
        result[i].append(c//5)
        c=c%5
        result[i].append(c)
for i in range(n) :
    print(result[i][0],result[i][1],result[i][2],result[i][3])