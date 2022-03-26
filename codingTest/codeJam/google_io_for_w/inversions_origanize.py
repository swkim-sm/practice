import sys
Input = sys.stdin.readline
t = int(Input())
for test_case in range(1, t+1):
    n = int(Input())
    board = [Input().rstrip() for _ in range(n*2)]
    
    ios = []
    for i in range(0, 2*n, n):
        for j in range(0, 2*n, n):
            i_cnt = 0
            for x in range(n):
                for y in range(n):
                    if board[i+x][j+y] == 'I':
                        i_cnt += 1
            ios.append([i_cnt, n**2-i_cnt])
    
    
    answer = 0
    answer += abs(ios[0][0]-ios[3][0])
    answer += abs(ios[1][0]-ios[2][0])
    # print(answer)
    print(f"Case #{test_case}: {answer}")