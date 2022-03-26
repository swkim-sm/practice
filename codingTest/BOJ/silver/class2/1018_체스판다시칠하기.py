import sys
Input = sys.stdin.readline
n, m = map(int, Input().split())
board = [Input().rstrip() for _ in range(n)]
answer = n*m
for i in range(n-7):
    for j in range(m-7):
        w_start_cnt = 0
        b_start_cnt = 0
        w_line =  'WB'*4
        b_line = 'BW'*4
        for x in range(8):
            for y in range(8):
                if x % 2:
                    if board[i+x][j+y] != w_line[y]:
                        w_start_cnt += 1
                    if board[i+x][j+y] != b_line[y]:
                        b_start_cnt += 1
                else:
                    if board[i+x][j+y] != b_line[y]:
                        w_start_cnt += 1
                    if board[i+x][j+y] != w_line[y]:
                        b_start_cnt += 1
        answer = min(w_start_cnt, b_start_cnt, answer)
print(answer)