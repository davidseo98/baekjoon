n = input()
total_num = ""
while 1:
    try:
        total_num += input()
    except:
        break
print(n)
total = 0
for i in range(len(total_num)):
    total += int(total_num[i])
print(total)
