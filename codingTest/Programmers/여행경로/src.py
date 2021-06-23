def solution(tickets):
    answer = ["ICN"]
    candidates = []
    n = len(tickets)
    visited = [False] * n

    def dfs(depart):
        if len(answer) == n + 1:
            candidates.append(list(answer))
            return
        for idx, ticket in enumerate(tickets):
            if depart == ticket[0] and not visited[idx]:
                answer.append(ticket[1])
                visited[idx] = True
                dfs(ticket[1])
                visited[idx] = False
                answer.pop()
    dfs("ICN")
    
    candidates.sort()
    answer = candidates[0]
    return answer
