import sys
n = int(input())
#300 60 10 
times = [300, 60, 10]
result = []
if n%10 != 0 :
    print(-1)
    sys.exit(1)
for time in times : 
    result.append(n//time)
    n = n%time
print(result[0], result[1], result[2])
    
