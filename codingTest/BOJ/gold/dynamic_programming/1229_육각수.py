import sys
from collections import deque
n = int(sys.stdin.readline())

dp = [1]
d = 5

while dp[-1]+d <= n:
    tmp = dp[-1] + d
    dp.append(tmp)
    d += 4

dq = deque([(n, 0, len(dp)-1)])
visited = [False for _ in range(n+1)]

while dq:
    cur, cnt, last_point = dq.popleft()
    if cur == 0:
        print(cnt)
        break
    for i in range(last_point, -1, -1):
        tmp = cur - dp[i]
        if tmp >= 0 and not visited[tmp]:
            dq.append((tmp, cnt+1, i))
            visited[tmp] = True