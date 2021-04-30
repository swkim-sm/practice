def solution(gems):
    answer = [0, 100000]
    num_type = len(set(gems))
    num_gems = len(gems)

    start = 0
    end = 0
    gem_cnt = {gems[0]:1}

    while start <= end:
        if len(gem_cnt) == num_type:
            if end-start < answer[1]-answer[0]:
                answer[0] = start+1
                answer[1] = end+1
            if gem_cnt[gems[start]] == 1:
                del gem_cnt[gems[start]]
            else:
                gem_cnt[gems[start]] -= 1

            start += 1
        elif end == num_gems - 1:
            break
        else:
            end += 1
            if gems[end] not in gem_cnt.keys():
                gem_cnt[gems[end]] = 1
            else:
                gem_cnt[gems[end]] += 1
    return answer
