import sys

n = int(sys.stdin.readline())
for _ in range(n):
    word = sys.stdin.readline().strip()
    start = 0
    end = len(word) - 1
    answer = 0
    is_similar = False
    is_false = False
    while start <= end + 1:
        if word[start] != word[end]:
            # print(word[start], word[end])
            if is_similar:
                is_false = True
                print(2)
                break
            if word[start + 1] == word[end]:
                is_similar = True
                start += 1
                continue
            if word[start] == word[end - 1]:
                is_similar = True
                end -= 1
                continue
            if not is_similar:
                print(2)
                is_false = True
                break
        end -= 1
        start += 1
    if is_similar and not is_false:
        print(1)
    if not is_similar and not is_false:
        print(0)
