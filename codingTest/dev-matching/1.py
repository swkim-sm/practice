def solution(dist):
    answer = []
    n = len(dist)
    right = [[dist[0][1], 1]] # (distance 0 to n, n)
    left = [[0, 0]]
    for i in range(2, n):
        _, r = right[-1]
        # 0보다 왼쪽에 위치한 경우
        if dist[r][i] == (dist[0][i] + dist[0][r]):
            left.append([-dist[0][i], i])
        
        else:
            right.append([dist[0][i], i])
    left.sort()
    right.sort()
    tmp = []
    for l in left:
        tmp.append(l[1])
    for r in right:
        tmp.append(r[1])
    
    answer.append(tmp)
    reversed_tmp = list(reversed(tmp))
    answer.append(reversed_tmp)
    answer.sort()
    return answer