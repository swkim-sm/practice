import sys
Input = sys.stdin.readline
n = int(Input())
A = list(map(int, Input().split()))
B = list(map(int, Input().split()))

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if A[i] > B[j]:
            dp[i][j] = max(dp[i][j+1]+B[j], dp[i+1][j+1], dp[i-1][j])
        else:
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
print(dp[0][0])


# top-down
# N = int(input())
# left =[0] +list(map(int, input().split()))
# right= [0]+list(map(int, input().split()))

# dp = [[0 for i in range(N+1)] for i in range(N+1)]

# for row in range(1,N+1):
#     for col in range(1,N+1):
#         if right[col] < left[row]:
#             dp[row][col] = max(dp[row][col-1] + right[col], dp[row-1][col], dp[row-1][col-1])
#         else:
#             dp[row][col] = max(dp[row-1][col], dp[row-1][col-1])

# print(dp[N][N])
# print(dp)


# score: 31
# def solution(l, r, ans):
#     if l == n or r == n:
#         return ans
    
#     tmp = 0
#     if A[l] > B[r]:
#         tmp = solution(l, r+1, ans+B[r])
#     tmp = max(tmp, solution(l+1, r+1, ans))
#     tmp = max(tmp, solution(l+1, r, ans))

#     return tmp

# print(solution(0, 0, 0))


# # greedy -> no optimal answer
# max_val = sorted(A)[-1]
# A = deque(A)

# while A and B:
#     x = A[0]
#     y = B[0]
#     if x > y:
#         answer += y
#         B.popleft()
#         continue

#     A.popleft()
#     if y >= max_val:
#         B.popleft()
