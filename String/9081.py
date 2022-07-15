import sys

t = int(sys.stdin.readline())
input_list = [sys.stdin.readline().strip() for _ in range(t)]
word_list = list()
for word in input_list:
    line = list()
    for i in range(len(word)):
        line.append(word[i])
    word_list.append(line)

for word in word_list:
    for i in range(len(word) - 1, 0, -1):
        if word[i] > word[i - 1]:
            idx = i
            for j in range(i, len(word)):
                if word[i - 1] < word[j]:
                    idx = j
            word[idx], word[i - 1] = word[i - 1], word[idx]
            word = word[:i] + sorted(word[i:])
            break
    print("".join(word))
