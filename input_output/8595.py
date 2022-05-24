n = int(input())
string = input()
numbers = list()
cur_num = ""

for i in range(n):
    if string[i].isnumeric():
        cur_num += string[i]
        if i == n - 1:
            numbers.append(int(cur_num))
    else:
        if cur_num != "":
            numbers.append(int(cur_num))
            cur_num = ""

if len(numbers) == 0:
    print(0)
else:
    print(sum(numbers))
