import sys

n = int(sys.stdin.readline().rstrip())
words = list()
for _ in range(n):
    words.append(sys.stdin.readline().rstrip())

words = list(set(words))
words.sort()
words.sort(key=lambda x: len(x))

for w in words:
    print(w)
