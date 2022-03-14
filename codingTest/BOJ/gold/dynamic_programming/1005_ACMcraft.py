import sys
from collections import defaultdict, deque
Input = sys.stdin.readline

T = int(Input())

for _ in range(T):
    # input
    N, K = map(int, Input().split())
    times = list(map(int, Input().split()))
    graph = defaultdict(list)
    in_degree = [0 for _ in range(N)]
    for _ in range(K):
        x, y = map(int, Input().split())
        graph[x-1].append(y-1)
        in_degree[y-1] += 1
    
    # perform
    dq = deque()
    dp = [0 for _ in range(N)]
    for i in range(N):
        if in_degree[i] == 0:
            dq.append(i)
            dp[i] = times[i]

    while dq:
        cur_building = dq.popleft()
        for i in graph[cur_building]:
            in_degree[i] -= 1
            dp[i] = max(dp[i], dp[cur_building]+times[i])
            if in_degree[i] == 0:
                dq.append(i)

    # output
    W = int(Input())-1
    print(dp[W])