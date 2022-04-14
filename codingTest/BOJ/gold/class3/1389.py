import sys
from collections import defaultdict, deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

arr = [[-1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dq = deque([[i, 0]])
    arr[i][i] = 0
    while dq:
        x, cnt = dq.popleft()
        cnt += 1
        for y in graph[x]:
            if arr[i][y] == -1:
                arr[i][y] = cnt
                dq.append([y, cnt])

answer = []
for i in arr:
    answer.append(sum(i))
print(answer.index(min(answer))+1)

## dfs (다른 사람 풀이)
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
adj = [list() for i in range(n+1)]
bacon = [[sys.maxsize] * (n+1) for i in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


def dfs(x, visited, path, origin, cnt):
    bacon[origin][x] = min(cnt, bacon[origin][x])
    for a in adj[x]:
        if not visited[a]:
            visited[a] = True
            if bacon[origin][a] > cnt + 1:
                dfs(a, visited, path + [a], origin, cnt + 1)
            visited[a] = False
    return cnt


result = sys.maxsize
person = -1
for i in range(1, n+1):
    visited = [False] * (n+1)
    dfs(i, visited, [], i, 0)
    s = sum(bacon[i][1:])
    if result > s:
        result = s
        person = i

print(person)

'''