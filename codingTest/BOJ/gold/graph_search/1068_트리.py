import sys
from collections import defaultdict, deque

Input = sys.stdin.readline

def bfs(n, parents, target):
    graph = defaultdict(list)
    if parents.index(-1) == target:
        return 0

    for i in range(n):
        graph[parents[i]].append(i)

    cnt = 0 # num of leaf nodes
    dq = deque([-1])

    while dq:
        cur = dq.popleft()
        
        if not len(graph[cur]):
            cnt += 1
            continue
        
        flag = True
        for child in graph[cur]:
            if child != target:
                dq.append(child)
                flag = False
        if flag:
            cnt += 1

    return cnt

N = int(Input())
parents = list(map(int, Input().split()))

target = int(Input())

print(bfs(N, parents, target))