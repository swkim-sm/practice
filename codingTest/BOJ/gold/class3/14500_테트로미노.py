import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def dfs(board, x, y, num_of_blocks, cnt, visited):
    global answer
    # 아래 두 줄 추가로 시간 1/3 
    if answer >= 1000*(4-num_of_blocks) + cnt:
        return
    if num_of_blocks == 4:
        answer = max(answer, cnt)
        return
    
    num_of_blocks += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(board, nx, ny, num_of_blocks, cnt+board[nx][ny], visited)
            visited[nx][ny] = False

answer = -1
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(board, i, j, 1, board[i][j], visited)
        visited[i][j] = False

for i in range(n):
    for j in range(m):
        tmp = board[i][j]
        dd = [board[i+dx[l]][j+dy[l]] for l in range(4) if (0 <= i+dx[l] < n and 0 <= j+dy[l] < m)]
        tmp += sum(dd)
        if len(dd) == 4:
            tmp -= min(dd)
        elif len(dd) < 3:
            continue
        answer = max(tmp, answer)            

print(answer)