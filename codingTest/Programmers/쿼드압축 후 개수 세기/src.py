def solution(arr):
    answer = [0, 0]
    zip_arr = []
    arr_n = len(arr[0])
    part_n = arr_n

    visited = [[0]*arr_n for _ in range(arr_n)]

    # 전체 개수 확인
    for i in range(arr_n):
        for j in range(arr_n):
            if arr[i][j] == 0:
                answer[0] += 1
            else:
                answer[1] += 1

    while True:
        # 종료 조건
        if part_n == 1:
            break
        zipped_0 = 0
        zipped_1 = 0
        # 같은 수인지 확인
        for i in range(0, arr_n, part_n):
            for j in range(0, arr_n, part_n):
                if visited[i][j] == 0:
                    flag = False
                    zero_one = arr[i][j]
                    for ii in range(i, i+part_n):
                        for jj in range(j, j+part_n):
                            if arr[ii][jj] != zero_one:
                                flag = True
                                break
                        if flag:
                            break
                    if not flag:
                        for ii in range(i, i+part_n):
                            for jj in range(j, j+part_n):
                                visited[ii][jj] = 1
                        if zero_one == 0:
                            zipped_0 += 1
                        else:
                            zipped_1 += 1

        # 다음 진행을 위해 n 업데이트
        part_n //= 2
        zip_arr.append([zipped_0, zipped_1])

    for idx, val in enumerate(zip_arr):
        if val[0] != 0:
            answer[0] -= val[0]*(arr_n**2) - val[0]
        if val[1] != 0:
            answer[1] -= val[1]*(arr_n**2) - val[1]
        arr_n //= 2
    return answer
