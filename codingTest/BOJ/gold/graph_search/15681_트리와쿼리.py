import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
Input = sys.stdin.readline

n, r, q = map(int, Input().split())
graph = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, Input().split())
    graph[u].append(v)
    graph[v].append(u)

queries = []
for _ in range(q):
    queries.append(int(Input()))

def dfs(visited, graph, cur, dp):
    cnt = 1
    visited[cur] = True
    for child in graph[cur]:
        if not visited[child]:
            visited[child] = True
            cnt += dfs(visited, graph, child, dp)
    dp[cur] = cnt
    return dp[cur]

visited = [False for _ in range(n+1)]
dp = [0 for _ in range(n+1)]

dfs(visited, graph, r, dp)

for query in queries:
    print(dp[query])