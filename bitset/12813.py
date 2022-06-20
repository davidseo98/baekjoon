a = input()
b = input()

result = ["" for _ in range(5)]

for i in range(len(a)):
    result[0] += str(int(bool(int(a[i]) and int(b[i]))))
    result[1] += str(int(bool(int(a[i]) or int(b[i]))))
    result[2] += str(int(bool(int(a[i]) != (int(b[i])))))
    result[3] += str(int(bool(not int(a[i]))))
    result[4] += str(int(bool(not int(b[i]))))

for r in result:
    print(r)
