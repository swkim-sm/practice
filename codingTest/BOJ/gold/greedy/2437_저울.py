import sys
Input = sys.stdin.readline

N = int(Input())
weights = list(map(int, Input().split()))
weights.sort()
target = 1
for weight in weights:
    if target < weight:
        break
    target += weight
print(target)
