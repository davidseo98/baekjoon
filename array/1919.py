string1 = input()
string2 = input()

string1_list = list()
string2_list = list()
total_len = len(string1) + len(string2)

for i in range(len(string1)):
    string1_list.append(string1[i])

for i in range(len(string2)):
    string2_list.append(string2[i])

both_count = 0
for letter in string2_list:
    if letter in string1_list:
        both_count += 1
        string1_list.remove(letter)

print(total_len-both_count*2)
