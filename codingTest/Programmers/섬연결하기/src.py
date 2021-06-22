from collections import deque
def solution(n, costs):
    answer = 0

    visited = set()
    costs.sort(key=lambda x:x[2])
    visited.add(costs[0][0])
    while len(visited) < n:
        for i, (x, y, c) in enumerate(costs):
            if (x in visited) and (y in visited):
                continue
            if (x in visited) or (y in visited):
                visited.update([x, y])
                answer += c
                del costs[i]
                break

    return answer
