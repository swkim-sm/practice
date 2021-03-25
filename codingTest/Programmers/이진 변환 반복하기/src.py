def solution(s):
    answer = [0, 0] # [이진변환 횟수, 변환 과정에서 제거된 0 개수]
    result = s

    while result != "1":
        # 반복 횟수
        answer[0] += 1

        # 0 제거
        before = len(result)
        result = result.replace("0", "")
        after = len(result)
        answer[1] += (before - after)

        # 이진 변환
        tmp_result = ""
        while after != 0:
            r = after%2
            after //= 2
            tmp_result = str(r) + tmp_result

        result = tmp_result

    return answer
