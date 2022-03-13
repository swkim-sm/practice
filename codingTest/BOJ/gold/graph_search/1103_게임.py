import sys
Input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, Input().split())
board = []
for _ in range(N):
    board.append(list(Input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

def dfs(x, y, n, cnt):
    global answer
    if answer == -1:
        return
    visited[x][y] = True
    for i in range(4):
        nx = x + n*dx[i]
        ny = y + n*dy[i]
        if 0 <= nx < N and 0 <= ny < M and dp[nx][ny] < cnt+1:
            if board[nx][ny] == 'H':
                continue
            elif visited[nx][ny]:
                answer = -1
                return
            else:
                dp[nx][ny] = cnt+1
                visited[nx][ny] = True
                dfs(nx, ny, int(board[nx][ny]), cnt+1)
                visited[nx][ny] = False

    visited[x][y] = False
    if answer == -1:
        return
    else: 
        answer = max(answer, cnt)


visited = [[False for _ in range(M)]for _ in range(N)]
dp = [[0 for _ in range(M)]for _ in range(N)]

dfs(0, 0, int(board[0][0]), 1)

print(answer)