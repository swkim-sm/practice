from collections import deque

def solution(n, edge):
    answer = 0
    visited = [-1]*(n+1)
    adj = [[] for _ in range(n+1)]
    for e1, e2 in edge:
        adj[e1].append(e2)
        adj[e2].append(e1)

    dq = deque([[1, 0]])
    while dq:
        tmp_val, tmp_cnt = dq.popleft()
        if visited[tmp_val] == -1:
            visited[tmp_val] = tmp_cnt
            tmp_cnt += 1
            for a in adj[tmp_val]:
                dq.append([a, tmp_cnt])

    max_visited = max(visited)
    for v in visited:
        if v == max_visited:
            answer += 1

    return answer
