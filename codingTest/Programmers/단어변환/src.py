from collections import deque
def solution(begin, target, words):
    answer = 0
    n = len(words) # words 개수
    m = len(begin) # 단어 길이
    visited = [False]*n
    
    dq = deque([[begin, 0]])
    
    while dq:
        cur, cnt = dq.popleft()
        if cur == target:
            return cnt
        cnt += 1
        for i in range(n):
            # 단어 비교
            same = 0
            for j in range(m):
                if words[i][j] != cur[j]:
                    same += 1
                    if same > 1:
                        break
            if same == 1 and not visited[i]:
                dq.append([words[i], cnt])
                visited[i] = True
    return answer
