import sys
from collections import deque
Input = sys.stdin.readline
n, m = map(int, Input().split())
board = [[0 for _ in range(n+1)]for _ in range(n+1)]

for _ in range(n-1):
    x, y, cost = map(int, Input().split())
    board[x][y] = cost
    board[y][x] = cost

for _ in range(m):
    x, y = map(int, Input().split())
    dq = deque([(x, 0)])
    visited = [False for _ in range(n+1)]
    visited[x] = True
    while dq:
        node, cost = dq.popleft()
        if node == y:
            print(cost)
            break
        for i in range(1, n+1):
            if not visited[i] and board[node][i]:
                dq.append((i, cost+board[node][i]))
                visited[i] = True