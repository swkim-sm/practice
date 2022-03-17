import sys
Input = sys.stdin.readline
n, m, k = map(int, Input().split())
board = []
for _ in range(n):
    board.append(list(Input().rstrip()))
target = Input().rstrip()

dx = []
dy = []

for i in range(1, k+1):
    tx = [-i, i, 0, 0]
    ty = [0, 0, -i, i]
    dx.extend(tx)
    dy.extend(ty)

visited = [[[-1 for _ in range(m)]for _ in range(n)] for _ in range(len(target))]

def dfs(x, y, idx):
    global answer
    if idx == len(target)-1:
        return 1

    if visited[idx][x][y] != -1:
        return visited[idx][x][y]

    visited[idx][x][y] = 0
    for i in range(k*4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == target[idx+1]:
            visited[idx][x][y] += dfs(nx, ny, idx+1)
    
    return visited[idx][x][y]

answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == target[0]:
            answer += dfs(i, j, 0)
print(answer)