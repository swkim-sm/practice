def solution(n, times):
    answer = 0
    times.sort()
    
    # 이진탐색을 위한 최솟값과 최댓값 설정
    # 이진탐색할 대상은 시간
    left = 1 
    right = times[0]*n
    
    # 이진탐색
    while left <= right:
        # 중간값
        mid = (left+right)//2
        
        # mid 시간 안에 n명을 모두 심사할 수 있는지 확인
        cnt = 0
        for time in times:
            cnt += (mid // time)
            if cnt >= n:
                break
        
        # 심사할 수 있다면 그 시간을 저장하고
        # 더 짧은 시간 내에 심사할 수 있는지 확인
        if cnt >= n:
            answer = mid
            right = mid - 1
        # 심사할 수 없다면 최소 시간을 늘려서 다시 확인
        else:
            left = mid + 1
    return answer
