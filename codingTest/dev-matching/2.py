from collections import deque
from itertools import product
def solution(grid):
    n = len(grid)
    m = len(grid[0])

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def check_connection(tmp_grid):
        visited = [[0 for _ in range(m)] for _ in range(n)]
        v = 1
        break_flag = False

        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0:
                    visited[i][j] = v
                    k = tmp_grid[i][j]
                    dq = deque([(i, j)])
                    while dq:
                        x, y = dq.popleft()
                        for l in range(4):
                            nx = x + dx[l]
                            ny = y + dy[l]
                            if 0 <= nx < n and 0 <= ny < m and \
                            visited[nx][ny] == 0 and tmp_grid[nx][ny] == k:
                                visited[nx][ny] = v
                                dq.append((nx, ny))
                    v += 1
                if v == 5:
                    break_flag = True
                    break
            if break_flag:
                break

        for i in range(n):
            for j in range(m):
                if not visited[i][j] or visited[i][j] == 4:
                    return 0
        return 1
        
    
    tmp_grid = []
    for g in grid:
        tmp_grid.append(list(g))
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '?':
                cnt += 1
    prod = list(product(['a', 'b', 'c'], repeat=cnt))
    result = 0
    for p in prod:
        idx = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '?':
                    tmp_grid[i][j] = p[idx]
                    idx += 1
        if check_connection(tmp_grid):
            result += 1

    return result