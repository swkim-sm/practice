def solution(gems):
    answer = [0, 100000]
    uniq_num = len(set(gems))
    num = len(gems)
    
    start_idx = 0 
    while start_idx < num:
        tmp_arr = []
        cnt = 0
        last_idx = start_idx - 1
        flag = True
        for g in gems[start_idx:]:
            last_idx += 1
            if g not in tmp_arr:
                cnt += 1
                tmp_arr.append(g)
            if cnt == uniq_num:
                flag = False
                cand = last_idx - start_idx
                if cand < answer[1]-answer[0]:
                    answer = [start_idx+1, last_idx+1]
                break
        if flag:
            break
        start_idx += 1
    return answer
