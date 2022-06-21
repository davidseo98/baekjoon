import sys


n = int(sys.stdin.readline())
card_list = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
search_list = list(map(int, sys.stdin.readline().split()))

for s in search_list:
    print(int(s in card_list), end=" ")
