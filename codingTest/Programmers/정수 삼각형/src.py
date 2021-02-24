def solution(triangle):
    answer = 0
    for idx_i, val_i in enumerate(triangle):
        if idx_i == 0 : pass
        else:
            for idx_j, val_j in enumerate(val_i):
                # 왼 끝
                if idx_j == 0:
                    triangle[idx_i][idx_j] += triangle[idx_i-1][idx_j]
                # 오른 끝
                elif idx_j == idx_i:
                    triangle[idx_i][idx_j] += triangle[idx_i-1][idx_j-1]
                # 양 끝 제외
                else:
                    if triangle[idx_i-1][idx_j-1] > triangle[idx_i-1][idx_j]:
                        triangle[idx_i][idx_j] += triangle[idx_i-1][idx_j-1]
                    else:
                        triangle[idx_i][idx_j] += triangle[idx_i-1][idx_j]

    for x in triangle[len(triangle)-1]:
        if x > answer:
            answer = x
    return answer
