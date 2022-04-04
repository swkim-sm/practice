import sys
input = sys.stdin.readline
while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    
    candies = [[0, 0]+list(map(int, input().split())) for _ in range(m)]
    dp = [[0 for _ in range(n+2)] for _ in range(m)]

    # max sum of each row
    for i in range(m):
        for j in range(2, n+2):
            dp[i][j] = max(candies[i][j]+dp[i][j-2], dp[i][j-1])

    if m > 1:
        dp[1][-1] = max(dp[0][-1], dp[1][-1])
    # possible combinations of rows for max sum
    for i in range(2, m):
        dp[i][-1] = max(dp[i-2][-1]+dp[i][-1], dp[i-1][-1])

    print(dp[-1][-1])