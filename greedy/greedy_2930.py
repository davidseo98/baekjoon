r = int(input())
s = input()
n = int(input())
result = 0
windict = {"R":"P", "S":"R", "P":"S"}
option = ["S","R","P"]
most = {}
best = 0
for i in range(r) :
    most[i] = []
for i in range(n) :
    f = input()
    for j in range(r) :
        most[j].append(f[j])
        if s[j] == f[j] :
            result +=1
        elif windict[f[j]] == s[j] :
            result += 2

for i in range(r) :
    best_round_score = 0
    for item in option :
        round_score = 0
        for j in range(n) :
            if most[i][j] == item :
                round_score += 1
            elif item == windict[most[i][j]] :
                round_score += 2
        if round_score > best_round_score :
            best_round_score = round_score
    best += best_round_score

print(result)
print(best)
