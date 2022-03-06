import sys

# input
I = sys.stdin.readline
R, C = map(int, I().split())
visited = [0] * 26
board = [list(map(lambda x: ord(x)-65, I().rstrip())) for _ in range(R)]

# perform
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, n):
    global answer
    answer = max(n, answer)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and \
            visited[board[nx][ny]] == 0:
                visited[board[nx][ny]] = 1
                dfs(nx, ny, n+1)
                visited[board[nx][ny]] = 0


# output
answer = 0
visited[board[0][0]] = 1
dfs(0, 0, 1)
print(answer)