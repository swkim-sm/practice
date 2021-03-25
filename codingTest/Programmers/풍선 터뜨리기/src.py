def solution(a):
    answer = 2
    n = len(a)
    l_idx = 0
    r_idx = n-1
    l_min = a[0]
    r_min = a[-1]

    # n이 3 이하일 때 특수 경우
    if n < 3:
        return n
    if n == 3:
        if a[1] > a[0] and a[1] > a[2]:
            return 2
        else:
            return 3

    # 왼쪽은 False, 오른쪽은 True
    flag = True

    while True:
        # 왼쪽값 업데이트
        if flag:
            if l_min < a[l_idx+1] and r_min < a[l_idx+1]:
                l_idx += 1
            elif l_min > a[l_idx+1]:
                l_idx += 1
                l_min = a[l_idx]
                answer += 1
            else:
                flag = False

        # 오른쪽값 업데이트
        if not flag:
            if l_min < a[r_idx-1] and r_min < a[r_idx-1]:
                r_idx -= 1
            elif r_min > a[r_idx-1]:
                r_idx -= 1
                r_min = a[r_idx]
                answer += 1
            else:
                flag = True
        # 종료 조건
        if l_idx == r_idx-1:
            break
    return answer
