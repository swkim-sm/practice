def solution(a):
    answer = 0
    for idx, val in enumerate(a):
        tmp_ahead = sorted(a[:idx])
        tmp_behind = sorted(a[idx+1:])
        
        if tmp_ahead and tmp_behind and val > tmp_ahead[0] and val > tmp_behind[0]:
            continue
        else:
            answer += 1
        
    return answer
