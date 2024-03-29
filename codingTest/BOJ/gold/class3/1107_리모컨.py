import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
m = int(input())
broken_btns = []
if m:
    broken_btns += list(map(int, input().split()))

answer = abs(n-100)
cnt = 0

# 작은수에서 큰수로 이동할땐 500,000 까지만 보면 되지만
# 반대로 큰수에서 작은수로 내려올수도 있으므로 1,000,000 까지 봐야함
for num in range(1000001): 
    flag = False
    for i in str(num):
        if i in broken_btns: # 해당 숫자가 번호를 눌러서 만들 수 없는 경우엔 스탑
            flag = True
            break
        # else: # 번호를 눌러서 만들 수 있는 경우엔
    	# min(기존답, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)
    if not flag:
        answer = min(answer, len(str(num)) + abs(num - n))
print(answer)