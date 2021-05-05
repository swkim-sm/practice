def solution(stones, k):
    answer = 0
    min_num = 1
    max_num = 200000000
    while min_num < max_num - 1:
        jump = 0
        mid = (min_num + max_num) // 2
        
        for s in stones:
            if s > mid:
                jump = 0
            else:
                jump += 1
                if jump == k:
                    max_num = mid
                    break
        if max_num != mid:
            min_num = mid
            
    answer = max_num
    return answer
