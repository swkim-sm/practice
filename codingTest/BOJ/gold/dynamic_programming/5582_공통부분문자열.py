import sys
Input = sys.stdin.readline

s1 = Input().rstrip()
s2 = Input().rstrip()

answer = 0
board = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
for i in range(1, len(s2)+1):
    for j in range(1, len(s1)+1):
        if s2[i-1] == s1[j-1]:
            board[i][j] = board[i-1][j-1] + 1          
            answer = max(answer, board[i][j])

print(board)