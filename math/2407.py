from re import I


n, m = map(int, input().split())
answer = 1
for _ in range(m):
    answer *= n
    n -= 1
for i in range(2, m + 1):
    answer = answer // i
print(answer)
