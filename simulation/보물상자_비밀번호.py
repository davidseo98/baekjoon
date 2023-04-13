
T = int(input())
converter = {str(num) : num for num in range(10)}
num = 10
for letter in "ABCDEF":
    converter[letter] = num
    num += 1

for test_case in range(1, T + 1):

    n, k = map(int, input().split())
    numbers = input().rstrip()
    candidates = set()
    length = n // 4

    for start in range(n): # 가능한 N개의 숫자 
        result = 0
        string = ""
        for i, idx in enumerate(range(start, start + length)):
            num = numbers[(idx % n)]
            result += converter[num] * 16 ** (length - 1 - i) # 10진수로 변환해서 더하기
            string += num

        candidates.add(result)

    answer = sorted(list(candidates), reverse=True)[k - 1] # k번째로 큰 수 
    
    print(f"#{test_case} {answer}")
