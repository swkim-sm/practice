import sys

s1, s2 = [sys.stdin.readline().strip() for _ in range(2)]

dp = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]

for j in range(1, len(s2)+1):
    for i in range(1, len(s1)+1):
        if s2[j-1] == s1[i-1]:
            dp[j][i] = dp[j-1][i-1] + 1
        else:
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])

print(dp[-1][-1])