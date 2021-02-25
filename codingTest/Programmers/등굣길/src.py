def solution(m, n, puddles):
    answer = 0

    # 경우의 수를 담을 경로
    wayhome = [[0]*(m+1) for i in range(0, n+1)]
    wayhome[1][1] = 1

    # 경우의 수 계산
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                wayhome[i][j] = 0
            else:
                wayhome[i][j] = wayhome[i-1][j]+wayhome[i][j-1]

    answer = wayhome[n][m]%1000000007
    return answer
