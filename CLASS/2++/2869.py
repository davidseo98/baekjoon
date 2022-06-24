import sys
import math

a, b, v = map(int, sys.stdin.readline().split())

v = v - a

days = math.ceil(v / (a - b))
days += 1

print(days)