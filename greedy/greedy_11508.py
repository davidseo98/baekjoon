n = int(input())
items = []
total  = 0
for i in range(n) :
    items.append(int(input()))
items.sort(reverse=True)

for i in range(len(items)) :
    if i%3 == 0 or i%3 == 1 :
        total += items[i]
print(total)
