import sys

n = int(sys.stdin.readline())
a, b, c, d = dict(), dict(), dict(), dict()
for _ in range(n):
    i1, i2, i3, i4 = map(int, sys.stdin.readline().split())
    if i1 in a.keys():
        a[i1] += 1
    else:
        a[i1] = 1

    if i2 in b.keys():
        b[i2] += 1
    else:
        b[i2] = 1

    if i3 in c.keys():
        c[i3] += 1
    else:
        c[i3] = 1

    if i4 in d.keys():
        d[i4] += 1
    else:
        d[i4] = 1

result = 0
for n1 in a.keys():
    for n2 in b.keys():
        for n3 in c.keys():
            for n4 in d.keys():
                if n1 + n2 + n3 + n4 == 0:
                    result += a[n1] * b[n2] * c[n3] * d[n4]
print(result)
