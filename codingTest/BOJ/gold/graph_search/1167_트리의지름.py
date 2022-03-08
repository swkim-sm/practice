import sys
from collections import defaultdict
Input = sys.stdin.readline

v = int(Input())
graph = defaultdict(list)
for _ in range(v):
    tmp = list(map(int, Input().split()))
    for i in range(1, len(tmp)-1, 2):
        graph[tmp[0]-1].append((tmp[i]-1, tmp[i+1]))


def dfs(start, graph, visited):
    for node, cost in graph[start]:
        if not visited[node]:
            visited[node] = visited[start] + cost  
            dfs(node, graph, visited)

def solution(x, n, graph):
    visited = [0 for _ in range(n)]
    dfs(x, graph, visited)
    visited[x] = 0
    u = visited.index(max(visited))
    visited = [0 for _ in range(n)]
    dfs(u, graph, visited)
    visited[u] = 0
    return max(visited)
    

print(solution(0, v, graph))