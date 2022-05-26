n = int(input())


for i in range(n):
    string = input()
    letters = list()
    for j in range(len(string)):
        if j == 0:
            letters.append(string[0].upper())
        else:
            letters.append(string[j])

    print("".join(letters))