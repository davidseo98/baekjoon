import sys
from collections import defaultdict

graph = defaultdict(dict)
n = int(sys.stdin.readline())
parent = n
child = -1

while True:
    n = sys.stdin.readline()
    if not n:
        break
    
    if child < parent:
        graph[parent]["L"] = child
    else:
        graph[parent]["R"] = child