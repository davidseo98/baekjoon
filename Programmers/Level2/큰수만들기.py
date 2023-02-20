def solution(number, k):

    n = len(number)
    number = list(map(int, list(number)))
    removed = set()
    cnt = 0
    
    stack = []
    for i in range(n - 1):
        stack.append((number[i], i))
        if number[i] < number[i + 1]:
            while stack and stack[-1][0] < number[i + 1]:
                _, idx = stack.pop()
                removed.add(idx)
                cnt += 1
                if cnt == k: break
        
        if cnt == k: break

    new = [number[i] for i in range(n) if i not in removed]  
    return "".join(list(map(str, new)))[:len(new) - (k - cnt)]