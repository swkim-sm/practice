def solution(number, k):
    answer = ''
    int_num = list(map(int, number))
    n = len(number) - k
    start_idx = 0
    end_idx = k + 1
    # 길이가 n인 가장 큰 숫자 찾기
    for i in range(n):
        max_val = -1
        max_idx = 0
        for j in range(start_idx, end_idx):
            if int_num[j] > max_val:
                max_idx = j
                max_val = int_num[j]
                if int_num[j] == 9:
                    break
        answer += str(max_val)
        # print(max_idx, max_val)
        start_idx = max_idx + 1
        end_idx += 1
                
    return answer
