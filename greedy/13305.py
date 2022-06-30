import sys

n = int(sys.stdin.readline())
distances = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))

price = max(prices) + 1
total = 0
for i in range(n - 1):
    distance = distances[i]
    if price > prices[i]:
        price = prices[i]
        total += prices[i] * distance
        continue
    total += price * distance
    
print(total)
