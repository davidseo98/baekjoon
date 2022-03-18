import heapq as h

n = int(input())
cards = []
sum = 0
if n==1 :
    card = int(input())
elif n==2 :
    for i in range(2) :
        sum += int(input())
else : 
    for i in range(n) :
        h.heappush(cards, int(input()))

    while(1) :
        if len(cards) <= 1 :
            break
        min1 = h.heappop(cards)
        min2 = h.heappop(cards)
        new = min1 + min2 
        sum += new
        h.heappush(cards, new)
        
print(sum)
