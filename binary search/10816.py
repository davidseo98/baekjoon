import sys

n = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))
card_dict = dict()
for c in card_list:
    if c in card_dict.keys():
        card_dict[c] += 1
    else:
        card_dict[c] = 1

m = int(sys.stdin.readline())
search_list = list(map(int, sys.stdin.readline().split()))

key_set = list(card_dict.keys())
for s in search_list:
    if s in key_set:
        print(card_dict[s], end=" ")
    else:
        print(0, end=" ")
