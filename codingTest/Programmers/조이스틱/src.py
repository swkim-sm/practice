def solution(name):
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    n = len(name)
    answer = n-1
    updown = [0] * n
    curve = [False] * n
    
    # 각 자리에서 조이스틱 위아래 방향으로 움직이는 횟수
    for i in range(n):
        cur_cnt = alphabet.index(name[i])
        if cur_cnt > 13:
            updown[i] = 26 - cur_cnt
        else:
            updown[i] = cur_cnt
        answer += updown[i]
    print("one way", answer)
    
    # 최대 한 번 방향 전환 가능(A 만날 때)
    for i in range(n-1):
        tmp_ans = i*2 + (n-i) - 1
        # i 까지 전진
        for j in range(i+1):
            tmp_ans += updown[j]
        # 백
        start_flag = False
        for j in range(i+1, n):
            if updown[j] == 0 and not start_flag:
                tmp_ans -= 1
                continue
            else:
                start_flag = True
                tmp_ans += updown[j]
        
        print(tmp_ans)
        # answer과 min 값 저장
        answer = min(answer, tmp_ans)

    return answer
