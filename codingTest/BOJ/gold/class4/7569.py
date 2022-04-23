import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

move = [(1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)] # h, n, m

# bfs
dq = deque()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomatoes[z][y][x] == 1:
                dq.append((z, y, x))

while dq:
    z, y, x = dq.popleft()
    for i in range(6):
        nz = z + move[i][0]
        ny = y + move[i][1]
        nx = x + move[i][2]
        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
            if tomatoes[nz][ny][nx] == 0:
                tomatoes[nz][ny][nx] = tomatoes[z][y][x] + 1
                dq.append((nz, ny, nx))

ans = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomatoes[z][y][x] == 0:
                print(-1)
                exit()
            ans = max(ans, tomatoes[z][y][x])
print(ans-1)     