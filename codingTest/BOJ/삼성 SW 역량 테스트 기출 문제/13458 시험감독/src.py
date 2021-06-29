import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = N
for i in range(N):
    sub = A[i] - B
    answer += math.ceil(sub / C) if sub > 0 else 0

print(answer)
