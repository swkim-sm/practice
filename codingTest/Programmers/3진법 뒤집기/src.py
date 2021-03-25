def solution(n):
    answer = 0
    arr = []
    r = n

    # 3진법으로 바꾸기
    while n != 0:
        r = n % 3
        n = n // 3
        arr.append(r)

    sz = len(arr)-1
    # 10진법으로 표현
    for i, v in enumerate(arr):
        answer += (v*(3**(sz-i)))
    return answer
