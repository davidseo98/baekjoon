n = int(input())
dice = list(map(int, input().split()))
if n == 1 :
    total = sum(dice) - max(dice)
else :
    num_list = []
    num_list.append(min(dice[0],dice[5]))
    num_list.append(min(dice[1],dice[4]))
    num_list.append(min(dice[2],dice[3]))
    num_list.sort()
    one = num_list[0]
    two = sum(num_list[:2])
    three = sum(num_list[:3])
    print(num_list, one, two, three)
    total = one * (n-2)*(5*n-6) + two * (4+8*(n-2)) + three * 4
print(total)
