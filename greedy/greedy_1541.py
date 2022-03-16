s = input()
num = ''
numbers = []

for i in range(len(s)):
    if s[i].isnumeric() :
        num += s[i]
    else :
        numbers.append(int(num))
        numbers.append(s[i])
        num = ""
numbers.append(int(num))

sign = 0
total = 0
for item in numbers:
    if type(item) == int :
        if sign == 0 :
            total += item
        elif sign == 1 :
            total -= item

    elif item == "-" :
        if sign == 0:
            sign = 1

print(total)