def eval(gcd, array):
    for element in array:
        if element % gcd == 0:
            return False
    return True

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def get_gcd(array):
    result = array[0]
    for i in range(1, len(array)):
        result = gcd(result, array[i])
    
    return result


def solution(arrayA, arrayB):
    answer = 0
    
    a, b = get_gcd(arrayA), get_gcd(arrayB)
    is_pos1, is_pos2 = False, False
    
    if a: is_pos1 = eval(a, arrayB)
    if b: is_pos2 = eval(b, arrayA)
    if not is_pos1 and not is_pos2: return 0
    else: return max(a, b)
