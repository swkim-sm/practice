from itertools import combinations
N = int(input())
A = list(map(int, input().split()))

if N < 3:
    print(len(A))
    exit()

def check_func(arr, l, r):
    if r-l < 2 or l == r:
        return True
    for x in range(l, r):
        for y in range(x+1, r):
            for z in range(y+1, r+1):
                if arr[x]+arr[y] <= arr[z] or arr[y]+arr[z] <= arr[x] or arr[z]+arr[x] <= arr[y]:
                    return False
    return True

A.sort()
idx_combi = list(combinations([i for i in range(len(A))], 2))

answer = 0
for x, y in idx_combi:
    if check_func(A, x, y):
        answer = max(y-x+1, answer)

print(answer)
