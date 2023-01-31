def solution(arr1, arr2):
    
    m = len(arr1)
    n = len(arr2[0])
    t_arr2 = [[arr2[r][c] for r in range(len(arr2))] for c in range(len(arr2[0]))]
    answer = [[-1] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            val = sum(map(lambda x, y : x * y, arr1[i], t_arr2[j]))
            answer[i][j] = val
            
    return answer