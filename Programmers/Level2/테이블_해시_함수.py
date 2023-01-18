from functools import reduce

def solution(data, col, row_begin, row_end):
    
    answer = 0
    # 지정한 열로 정렬 + 첫번째 열로 정렬
    data.sort(key = lambda x : (x[col - 1], -x[0]))
    
    bits = []
    for row in range(row_begin - 1, row_end):
        result = [sum([data[row][i] % (row + 1) for i in range(len(data[row]))]) for row in range(row_begin - 1, row_end)]
        bits.append(result)
        
    for i in range(len(bits)):
        if i == 0: answer = bits[i]
        else: answer = answer ^ bits[i]
    
    return answer


def solution2(data, col, row_begin, row_end):
    
    answer = 0
    # 지정한 열로 정렬 + 첫번째 열로 정렬
    data.sort(key = lambda x : (x[col - 1], -x[0]))
    
    answer = reduce(lambda x, y: x ^ y,
                   [sum(map(lambda x : x % (row + 1), data[row])) for row in range(row_begin - 1, row_end)])
        
    return answer