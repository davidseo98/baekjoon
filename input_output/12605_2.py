n = int(input())
total_words = list()
for i in range(n):
    words = list(input().split())
    words = words[::-1]
    total_words.append(words)

for i in range(len(total_words)):
    string = " ".join(total_words[i])
    print(f"Case #{i+1}: {string}")
