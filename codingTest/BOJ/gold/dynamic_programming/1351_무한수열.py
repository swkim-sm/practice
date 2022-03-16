import sys
from collections import defaultdict

n, p, q = map(int, sys.stdin.readline().split())

dp = defaultdict(int)
dp[0] = 1

def solution(x):
    if dp[x] != 0:
        return dp[x]
    else:
        dp[x] = solution(x//p) + solution(x//q)
        return dp[x] 

print(solution(n))
