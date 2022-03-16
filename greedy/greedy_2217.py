n = int(input())
num_list = []
result = []

for i in range(n) :
    num_list.append(int(input()))

num_list.sort(reverse=True)

for i in range(n) :
    result.append(num_list[i] * (i+1))

print(max(result))
