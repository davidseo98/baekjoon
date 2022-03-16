n, k = map(int, input().split())
change = []
cnt = 0

for i in range(n) :
    change.append(int(input()))

change.sort(reverse=True)

for c in change : 
    cnt += k//c
    k = k % c

print(cnt)