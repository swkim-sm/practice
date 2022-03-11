import sys
N = int(sys.stdin.readline())

dp = [0 for _ in range(31)]

dp[0] = 1
dp[1] = 1

for i in range(2, 31):
    dp[i] = dp[i-1] + dp[i-2]*2

answer = 0
if N == 1:
    result = 1
elif N == 2:
    result = 3

elif N % 2:
    result = (dp[N] + dp[int((N-1)/2)]) / 2
else: 
    result = (dp[N] + dp[int(N/2)] + dp[int((N-2)/2)]*2) / 2

print(int(result))
