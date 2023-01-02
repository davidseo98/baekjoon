import sys

n = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(n)]
num_list.sort() # [5, 6, 7]
diff_list = list()

left, right, count, best = 0, 0, 0, -1
while right < n - 1:
    
    diff = num_list[right + 1] - num_list[right]
    diff_list.append(diff - 1)
    right += 1

print(diff_list)