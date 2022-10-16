# Two-Pointer
# 투 포인터 사이에 있는 보석들에 대한 정보를 저장한 리스트와 사전을 통해 효율성 달성


def solution(gems):

    gem2index = dict()
    cnt = 0
    for gem in gems:
        if gem not in gem2index.keys():
            gem2index[gem] = cnt
            cnt += 1

    gem_count = [0] * cnt
    total_gem_set = set(gems)
    start, end, p_start, p_end = 0, 0, -1, -1
    best = float("inf")
    answer = [-1, -1]
    n = len(gems)

    cur_gem_set = {gems[0]}
    gem_count[gem2index[gems[0]]] = 1

    while 1:

        if cur_gem_set == total_gem_set:

            if end - start < best:
                best = end - start
                answer = [start + 1, end + 1]

            cur_gem = gems[start]
            gem_count[gem2index[cur_gem]] -= 1

            if gem_count[gem2index[cur_gem]] == 0:
                cur_gem_set.remove(cur_gem)

            start += 1

        else:

            if end < n - 1:
                next_gem = gems[end + 1]

                if gem_count[gem2index[next_gem]] == 0:
                    cur_gem_set.add(next_gem)

                gem_count[gem2index[next_gem]] += 1
                end += 1

        if p_start == start and p_end == end:
            break

        p_start, p_end = start, end

    return answer


if __name__ == "__main__":
    gem = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    print(solution(gem))
