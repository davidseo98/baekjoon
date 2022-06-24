import sys

n = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()
alphabet = "-abcdefghijklmnopqrstuvwxyz"
hash_value = 0
cnt = 0
for letter in string:
    for i in range(len(alphabet)):
        if letter == alphabet[i]:
            hash_value += i * (31**cnt)
    cnt += 1


print(hash_value % 1234567891)
