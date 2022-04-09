import sys
input = sys.stdin.readline
k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
arr.sort()

left = 1
right = arr[-1]

while left <= right:
    mid = (left+right)//2
    cnt = 0
    for a in arr:
        cnt += (a//mid)

    if cnt >= n:
        left = mid+1
        answer = mid
    else:
        right = mid-1

print(right)
