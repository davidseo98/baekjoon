n, m = map(int, input().split())

words = list()
for i in range(n):
    words.append(input())

compare = list()
for i in range(m):
    compare.append(input())

# print(words)
# print(compare)

cnt = 0
for w in compare:
    if w in words:
        cnt += 1

print(cnt)
