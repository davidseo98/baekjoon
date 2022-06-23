import sys

n = int(sys.stdin.readline())
num_dict = dict()
for _ in range(n):
    num = int(sys.stdin.readline())
    if num not in num_dict.keys():
        num_dict[num] = 1
    else:
        num_dict[num] += 1

sorted_key = sorted(list(num_dict.keys()))

is_odd = False if n % 2 == 0 else True
not_solved = True
count = -1

mean = 0
median = 0
mode = 0
max_freq = max(list(num_dict.values()))
max_freq_num = list()
ran = sorted_key[-1] - sorted_key[0]

for key in sorted_key:
    value = num_dict[key]
    mean += key * value

    count += value
    if not_solved:
        if is_odd:
            if count >= n // 2:
                median = key
                not_solved = False
        else:
            if count > n // 2 - 1 and median == 0:
                median += key
            if count > n // 2 and median > 0:
                median += key
                not_solved = False

    if value == max_freq:
        max_freq_num.append(key)


mean = round(mean / n)
if not (is_odd):
    median = median // 2

print(mean)
print(median)
if len(max_freq_num) > 1:
    print(sorted(max_freq_num)[1])
else:
    print(max_freq_num[0])
print(ran)
