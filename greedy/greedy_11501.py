
t = int(input()) 
result = []
temp = []
for i in range(t) :
    n = int(input()) 
    price = list(map(int, input().split()))
    profit = 0
    max = 0
    for i in range(n-1, -1, -1) :
        if price[i] > max :
            max = price[i]
        else :
            profit += max-price[i]
    result.append(profit)
for i in result :
    print(i)