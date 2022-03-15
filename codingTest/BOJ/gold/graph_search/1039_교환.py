from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

def bfs():
    visited = set()
    ans = 0
    qlen = len(dq)
    while qlen:
        x = dq.popleft()
        cur = list(str(x))
        for i, j in combi:
            tmp = cur[:]
            tmp[i], tmp[j] = cur[j], cur[i]
            if tmp[0] == '0':
                continue
            nx = int(''.join(tmp))
            if nx not in visited:
                ans = max(ans, nx)
                visited.add(nx)
                dq.append(nx)
        qlen -= 1
    return ans

n, k = map(int, input().split())
item = [i for i in range(len(str(n)))]
combi = list(combinations(item, 2))
dq = deque()
dq.append(n)

ans = 0
for _ in range(k):
    ans = bfs()

if not ans:
    print(-1)
else:
    print(ans)