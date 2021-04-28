from collections import deque
def BFS(visited, computers, parent, n):
    visited[parent] = True
    q = deque([parent])
    while q:
        p = q.popleft()
        visited[p] = True
        for i in range(n):
            if computers[p][i] == 1 and not visited[i]:
                q.append(i)
                
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i] :
            BFS(visited, computers, i, n)
            answer += 1
    return answer
