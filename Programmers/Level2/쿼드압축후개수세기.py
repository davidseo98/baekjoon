def compress(arr, x, y):
    values = [arr[x][y], arr[x + 1][y], arr[x][y + 1], arr[x + 1][y + 1]]
    zeros, ones = 0, 0
    for val in values:
        zeros += val[0]
        ones += val[1]
    
    if not zeros or not ones:
        return [1, 0] if zeros else [0, 1]
    else:
        return [zeros, ones]
    
    
def init(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j]:
                arr[i][j] = [0, 1]
            else:
                arr[i][j] = [1, 0]

def solution(arr):

    init(arr)

    length = len(arr)
    while length > 1:
        temp = []
        for i in range(0, length, 2):
            line = []
            for j in range(0, length, 2):
                line.append(compress(arr, i, j))
            temp.append(line)
        arr = temp
        length = len(arr)
        
    return arr[0][0]