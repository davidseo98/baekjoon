total_strings = list()
result = list()

while 1:
    try:
        string = input()
        total_strings.append(string)
    except:
        break

for string in total_strings:
    upper_count = 0
    lower_count = 0
    digit_count = 0
    white_count = 0

    for i in range(len(string)):
        letter = string[i]
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1
        elif letter.isspace():
            white_count += 1
        else:
            digit_count += 1

    result.append((lower_count, upper_count, digit_count, white_count))

for row in result :
    for count in row :
        print(count, end=" ")
    print()
