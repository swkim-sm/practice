import sys
Input = sys.stdin.readline
N = int(Input())
arr = list(map(int, Input().split()))
S = int(Input())

for i in range(N-1):
    if S == 0:
        break
    max_val = arr[i]
    max_idx = i
    for j in range(i+1, min(N, i+S+1)):
        if arr[j] > max_val:
            max_val = arr[j]
            max_idx = j
    
    S -= (max_idx-i)
    for j in range(max_idx, i, -1):
        arr[j] = arr[j-1]
    arr[i] = max_val

print(' '.join(list(map(str, arr))))