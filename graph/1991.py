from collections import deque, defaultdict
import sys

def preorder():
    result = ""
    stack = deque(["A"])
    while stack:
        print(stack)
        cur = stack.pop()
        result += cur
        for child in graph[cur]:
            if child != ".": stack.append(child)
    
    return result

def inorder():
    
n = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(n):
    parent, left, right = sys.stdin.readline().rstrip().split()
    graph[parent].append(right)
    graph[parent].append(left)
print(graph)
print(preorder())
