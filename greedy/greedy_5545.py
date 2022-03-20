n = int(input())
d, t = map(int, input().split())
dough  = int(input())
total_kcal = dough
total_price = d
cur_val = total_kcal/total_price
toppings = []
for i in range(n):
    toppings.append(int(input()))

toppings.sort(reverse=True)
for topping in toppings :
    if (total_kcal+topping)/(total_price+t) > cur_val :
        total_kcal += topping
        total_price += t 
        cur_val = total_kcal/total_price
print(total_kcal//total_price)