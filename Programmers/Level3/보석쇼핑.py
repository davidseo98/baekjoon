from collections import defaultdict, deque
  
        
def solution(gems):
    
    answer = [0, 100001]
    gem_cnt = len(set(gems))
    
    if gem_cnt == 1: return [1, 1] # 고유 보석의 개수가 1인 경우

    cur_cnt = 0
    cnt_dict = defaultdict(int)
    queue = deque([])
    
    for i, g in enumerate(gems):
        
        if cnt_dict[g] == 0: cur_cnt += 1 # 없던 보석이 추가되는 경우
        
        cnt_dict[g] += 1
        queue.append(i)
        
        while queue and cur_cnt == gem_cnt:

            if len(queue) > 1 and queue[-1] - queue[0] < answer[1] - answer[0]:
                answer = [queue[0] + 1, queue[-1] + 1]
            
            cur = queue.popleft()
            if cnt_dict[gems[cur]] == 1:
                queue.appendleft(cur)
                break
            cnt_dict[gems[cur]] -= 1

    return answer