n = int(input())
string = input()
numbers = "0123456789"
result = ""
for i in range(n):
    if string[i] in numbers:
        result += string[i]
    else:
        result += " "

print(sum(list(map(int, result.split()))))
