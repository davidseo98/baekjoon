import sys

poke_num, prob_num = map(int, sys.stdin.readline().rstrip().split())
pokemon_dict = dict()
pokemon_list = list()
cnt = 1
for i in range(poke_num):
    input_str = sys.stdin.readline().rstrip()
    pokemon_dict[input_str] = cnt
    cnt += 1
    pokemon_list.append(input_str)

for i in range(prob_num):
    input_str = sys.stdin.readline().rstrip()
    if input_str.isnumeric():
        print(pokemon_list[int(input_str) - 1])
    else:
        print(pokemon_dict[input_str])
