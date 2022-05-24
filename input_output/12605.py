n = int(input())
inputs = list()
for i in range(n):
    words = list(input().split())
    inputs.append(words)

for i in range(n):
    print(f"Case #{i+1}:", end=" ")
    for j in range(len(inputs[i]) - 1, -1, -1):
        print(inputs[i][j], end=" ")
    print()
