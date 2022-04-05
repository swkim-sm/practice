import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

visited = [[False for _ in range(m)] for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            connected = deque([(i, j)])
            dq = deque([(i, j)])
            flag = False
            visited[i][j] = True
            tmp_visited = [[False for _ in range(m)] for _ in range(n)]
            tmp_visited[i][j] = True
            while dq:
                x, y = dq.popleft()
                for l in range(8):
                    nx = x + dx[l]
                    ny = y + dy[l]
                    if 0<=nx<n and 0<=ny<m:
                        if board[nx][ny] == board[i][j] and not tmp_visited[nx][ny]:
                            dq.append((nx, ny))
                            connected.append((nx, ny))
                            tmp_visited[nx][ny] = True
                            visited[nx][ny] = True
                        elif board[nx][ny] > board[x][y]:
                            flag = True
                            break
                        else:
                            tmp_visited[nx][ny] = True
                if flag:
                    break
            if not flag:
                answer += 1
                while connected:
                    x, y = connected.popleft()
                    for l in range(8):
                        nx = x + dx[l]
                        ny = y + dy[l]
                        if 0<=nx<n and 0<=ny<m and not tmp_visited[nx][ny]:
                            if board[nx][ny] <= board[x][y]:
                                tmp_visited[nx][ny] = True
                                connected.append((nx, ny))

print(answer)

## dfs 다른 사람 코드
'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(x, y):
  global top
  
  visited[x][y] = True

  for d in dir:
    dx = x+d[0]; dy = y+d[1]
    if 0<=dx<n and 0<=dy<m:
      if farm[x][y] < farm[dx][dy]:
        top = False
      elif farm[x][y] == farm[dx][dy] and not visited[dx][dy]:
        dfs(dx, dy)
  
if __name__ == '__main__':
  n, m = map(int, input().strip().split())
  farm = [list(map(int, input().strip().split())) for _ in range(n)]
  
  visited = [[0]*m for _ in range(n)]

  dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
  
  result = 0
  for i in range(n):
    for j in range(m):
      if not visited[i][j]:
        top = True
        dfs(i, j)
        if top:
          result += 1
  print(result)
  
'''

