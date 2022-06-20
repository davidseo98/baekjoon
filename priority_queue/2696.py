import sys
import heapq

test_num = int(sys.stdin.readline().rstrip())
for i in range(test_num):
    element_num = int(sys.stdin.readline().rstrip())
    read_count = element_num // 10
    elements = list()
    for j in range(read_count + 1):
        elements += list(map(int, sys.stdin.readline().rstrip().split()))
    print_count = (
        len(elements) // 2 if len(elements) % 2 == 0 else len(elements) // 2 + 1
    )
    print(print_count)
    # print(elements)

    front_heap = list()
    back_heap = list()
    front_count, back_count = 0, 0
    is_odd = True
    result = list()
    for num in elements:

        if front_count == 0:
            front_heap.append(-num)
            front_count += 1
            result.append(num)
            is_odd = not (is_odd)
            continue

        front_max = -front_heap[0]

        if num > front_max:
            if front_count > back_count:
                heapq.heappush(back_heap, num)
                back_count += 1
            elif front_count == back_count:
                heapq.heappush(back_heap, num)
                heapq.heappush(front_heap, -heapq.heappop(back_heap))
                front_count += 1
        else:
            if front_count > back_count:
                heapq.heappush(front_heap, -num)
                heapq.heappush(back_heap, -heapq.heappop(front_heap))
                back_count += 1
            elif front_count == back_count:
                heapq.heappush(front_heap, -num)
                front_count += 1
        # print(front_heap, back_heap)

        if is_odd:
            result.append(-front_heap[0])
        is_odd = not (is_odd)
    cnt = 0
    for r in result:
        if cnt == 10:
            print()
        print(r, end=" ")
        cnt += 1
    print()
