def solution(people, limit):
    answer = 0
    people.sort()
    l = 0
    r = len(people) - 1
    while l <= r:
        tmp_sum = people[l] + people[r]
        
        if tmp_sum > limit:
            r -= 1
        else:
            l += 1
            r -= 1
        
        answer += 1 
        
            
    return answer
