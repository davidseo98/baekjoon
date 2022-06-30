import sys
from collections import Counter

n = int(sys.stdin.readline())
letter_dict = dict()
words_list = list()
max_length = 0
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    words_list.append(word)
    if len(word) > max_length:
        max_length = len(word)

for i in range(n):
    diff = max_length - len(words_list[i])
    words_list[i] = "0" * diff + words_list[i]

letters_by_loc = [[] for _ in range(max_length)]
for i in range(max_length):
    for j in range(n):
        letter = words_list[j][i]
        if letter == "0":
            continue
        letters_by_loc[i].append(letter)

for i in range(max_length):
    letters = letters_by_loc[i]
    for letter in Counter(letters).most_common():
        if letter[0] in letter_dict.keys():
            letter_dict[letter[0]] += 10 ** (max_length - i - 1) * letter[1]
        else:
            letter_dict[letter[0]] = 10 ** (max_length - i - 1) * letter[1]

letters_count = list()
for letter in letter_dict.items() :
    letters_count.append(letter)
letters_count.sort(key = lambda x : x[1], reverse= True) 

letter_value = dict()
value = 9
for letter in letters_count :
    letter_value[letter[0]] = value
    value -= 1

answer = 0
for word in words_list : 
    string = ""
    for i in range(len(word)) :
        if word[i] == "0" :
            continue
        string += str(letter_value[word[i]])
    answer += int(string)
print(answer)
