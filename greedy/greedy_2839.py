n = int(input())

impossible = 1
max_five = n//5
for i in range(max_five,-1,-1) :
    with_five = 5 * i 
    rest = n - with_five
    if rest%3 == 0 :
        three = rest // 3
        five = i
        impossible = 0
        break

if impossible :
    print(-1)
else :
    print(five+three)