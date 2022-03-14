import sys
Input = sys.stdin.readline

T = int(Input())
targets = []

for _ in range(T):
    targets.append(int(Input()))

dp = [1, 1]
while True:
    new_elem = dp[-1] + dp[-2]
    if new_elem > 1000000000:
        break
    else:
        dp.append(new_elem)

for target in targets:
    max_idx = len(dp)
    answer = []
    while target > 0:
        for i in range(max_idx-1, 0, -1):
            if dp[i] <= target:
                max_idx = i
                target -= dp[i]
                answer.append(dp[i])
                break
    answer.sort()
    print(' '.join(list(map(str, answer))))