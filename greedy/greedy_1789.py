# 200 = 1,2, ...., 18 + 나머지를 채워주는 숫자

n = int(input())
i = 1
result = 0
while(1) :
    temp = (i * (i+1))//2
    if temp > n :
        i -= 1
        break
    i += 1

while(1) :
    res = n - (i*(i+1))//2
    if res <= i :
        result = i
        break
    else :
        i += 1
print(result)

