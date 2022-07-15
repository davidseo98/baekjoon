s = input()
t = input()
for _ in range(len(t) - len(s)):
    if t[-1] == "A":
        t = t[: len(t) - 1]
    else:
        t = t[: len(t) - 1][::-1]
print(int(s == t))
