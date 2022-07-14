from hashlib import new
import sys

string = sys.stdin.readline().strip()

if "<" not in string:
    for word in string.split():
        print(word[::-1], end=" ")
    exit()

new_string = ""
ignore = False
word = ""
for i in range(len(string)):
    if ignore:
        new_string += string[i]
        if string[i] == ">":
            ignore = False
        continue
    if string[i] == "<":
        if word:
            for w in word.split():
                new_string += w[::-1] + " "
            new_string = new_string[: len(new_string) - 1]
            word = ""
        ignore = True
        new_string += string[i]
        continue
    if not (ignore):
        word += string[i]

if word:
    for w in word.split():
        new_string += w[::-1] + " "
    new_string = new_string[: len(new_string) - 1]
print(new_string)
