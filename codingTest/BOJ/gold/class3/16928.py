import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

visited = [False for _ in range(101)]
trick = [0 for _ in range(101)]
for _ in range(n+m):
    x, y = map(int, input().split())
    trick[x] = y

def bfs(dq):
    cur_cnt = len(dq)
    for _ in range(cur_cnt):
        cur = dq.popleft()
        if not visited[cur]:
            visited[cur] = True
            for i in range(1, 7):
                tmp = cur + i
                if tmp > 100:
                    break

                while trick[tmp]:
                    tmp = trick[tmp]
                    if tmp > 100:
                        break
                if not visited[tmp] and tmp not in dq:
                    dq.append(tmp)
            

dq = deque([1])
answer = 0
while dq:
    # break condition
    if 100 in dq:
        print(answer)
        break
    answer += 1
    bfs(dq)