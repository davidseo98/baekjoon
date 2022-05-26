string = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
count = [0] * len(alpha)

for i in range(len(string)):
    
    for j in range(len(alpha)):
        if string[i] == alpha[j]:
            count[j] += 1

for c in count:
    print(c, end=" ")
