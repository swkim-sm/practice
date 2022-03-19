import sys

w, h = map(int, sys.stdin.readline().split())
board = [[[0, 0] for _ in range(w+1)] for _ in range(h+1)] # (horizon, vertical)
board[1][1] = [1, 1]
for i in range(1, h+1):
    for j in range(1, w+1):
        if i == 1 and j != 1:
            board[i][j] = [1, 0]
            continue
        if i != 1 and j == 1:
            board[i][j] = [0, 1]
            continue
        # left to right
        board[i][j][0] += board[i][j-1][0] % 100000
        board[i][j][0] += board[i-1][j-1][1] % 100000
        # bottom to top
        board[i][j][1] += board[i-1][j][1] % 100000
        board[i][j][1] += board[i-1][j-1][0] % 100000

print(sum(board[h][w])%100000)
