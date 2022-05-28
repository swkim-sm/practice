import sys
from collections import deque
input = sys.stdin.readline

n, s, m = map(int, input().split())
diffs = list(map(int, input().split()))

dp = [[False for _ in range(m+1)] for _ in range(n+1)]
dp[0][s] = True

for i in range(n):
    for j in range(m+1):
        flag = dp[i][j]
        if flag:
            if j+diffs[i] <= m:
                dp[i+1][diffs[i]+j] = True
            if j-diffs[i] >= 0:
                dp[i+1][j-diffs[i]] = True

ans = -1
for i in range(m+1):
    if dp[n][i]:
        ans = i
print(ans)