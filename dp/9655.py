import sys

input = sys.stdin.readline

n = int(input())
rest = n % 4

print('SK') if rest == 1 or rest == 3 else print('CY')