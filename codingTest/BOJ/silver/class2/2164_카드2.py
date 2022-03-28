from collections import deque
n = int(input())
dq = deque([i for i in range(1, n+1)])
while len(dq) > 1:
    dq.popleft()
    tmp = dq.popleft()
    dq.append(tmp)
print(dq[-1])