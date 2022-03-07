import sys

Input = sys.stdin.readline

N, K = map(int, Input().split())
board = []

for n in range(N):
    board.append(list(map(lambda x: (int(x), 0), Input().split())))

S, X, Y = map(int, Input().split())

def solution(N, S, X, Y, board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for s in range(S):
        for i in range(N):
            for j in range(N):
                if board[i][j][0] == 0:
                    virus = 1001
                    for l in range(4):
                        nx = i + dx[l]
                        ny = j + dy[l]
                        if 0 <= nx < N and 0 <= ny < N \
                            and board[nx][ny][1] <= s \
                            and board[nx][ny][0] != 0:
                            virus = min(virus, board[nx][ny][0])
                    if virus != 1001:
                        board[i][j] = (virus, s+1)
                if i == X-1 and j == Y-1 and board[i][j][0]:
                    return board[i][j][0]


    return 0

print(solution(N, S, X, Y, board))
