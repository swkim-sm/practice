import sys
from collections import deque
Input = sys.stdin.readline
n, m = map(int, Input().split())
board = []
for _ in range(n):
    board.append(list(map(int, Input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    visited = [[False for _ in range(m)] for _ in range(n)]
    flag = True
    for i in range(1, n-1):
        for j in range(1, m-1):
            if board[i][j] != 0:
                cnt = 0
                flag = False
                visited[i][j] = True
                for l in range(4):
                    nx = i + dx[l]
                    ny = j + dy[l]
                    if not board[nx][ny] and not visited[nx][ny]:
                        cnt += 1
                board[i][j] = max(0, board[i][j]-cnt)
                if cnt == 4:
                    return 1 # isolated

    if flag:
        return -1 # melted all
def is_isolated(board):
    visited = [[False for _ in range(m)] for _ in range(n)]
    connect = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if board[i][j] and not visited[i][j]:
                visited[i][j] = True
                if connect > 0:
                    return True
                connect += 1
                dq = deque([(i, j)])
                while dq:
                    tx, ty = dq.popleft()
                    for l in range(4):
                        nx = tx + dx[l]
                        ny = ty + dy[l]
                        if 0 < nx < n-1 and 0 < ny < m-1:
                            if board[nx][ny] and not visited[nx][ny]:
                                visited[nx][ny] = True
                                dq.append((nx, ny))
    
    if connect > 1:
        return True
    return False


answer = 0
while True:
    if is_isolated(board):
        # print("isolated")
        break
    return_flag = bfs()
    if return_flag == 1:
        # print("isolated")
        break
    elif return_flag == -1:
        # print("all melted")
        answer = 0
        break
    answer += 1
    # print(board)
print(answer)