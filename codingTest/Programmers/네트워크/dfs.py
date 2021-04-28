def DFS(visited, computers, parent, n):
    visited[parent] = True
    for i in range(n):
        if computers[parent][i] == 1 and not visited[i]:
            DFS(visited, computers, i, n)
            
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i] :
            DFS(visited, computers, i, n)
            answer += 1
    return answer
