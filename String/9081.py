from itertools import permutations

n = int(input())

words = list()
for i in range(n):
    words.append(input())


def word2dict(word):
    letters = list()
    original = list()
    letters_dict = dict()
    for i in range(len(word)):
        letters.append(word[i])
        original.append(word[i])

    letters = sorted(list(set(letters)))
    for i in range(len(letters)):
        letters_dict[letters[i]] = i + 1

    for i in range(len(word) - 1, -1, -1):
        temp = list()
        part = word[i:]
        for j in range(len(part)):
            temp.append(part[j])
        # if "".join(sorted(temp)) != part :
        print(sorted(temp, reverse=True))
        print(part)
        # print(word[i:])

        # a = letters_dict[word[i]]
        # for j in range(i - 1, -1, -1):
        #    b = letters_dict[word[j]]
        #    if a > b:
        #        original[i], original[j] = original[j], original[i]
        #        #print(i,j, len(word))
        #        if j + 1 != len(word)-1 :
        #            original = original[: j + 1] + sorted(original[j + 1:])
        #        #original = original[: j + 1] + sorted(original[j + 1 :])
        #        return original


for word in words:
    l = word2dict(word)
    if l == None:
        print(word)
    else:
        print("".join(l))
