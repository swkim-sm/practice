def solution(n):
    answer = []
    path = [[-1, 0, 0]] # (x, y, num)
    cur_num = 1
    last_num = (n*(n+1))/2

    flag = 0
    for i in range(n, 0, -1):
        for j in range(i):
            # 좌하로 갈 때
            if flag % 3 == 0:
                path.append([path[-1][0]+1, path[-1][1], path[-1][2]+1])
            # 오른쪽으로 갈 때
            elif flag % 3 == 1:
                path.append([path[-1][0], path[-1][1]+1, path[-1][2]+1])
            # 좌상으로 갈 때
            else:
                path.append([path[-1][0]-1, path[-1][1]-1, path[-1][2]+1])

        flag += 1
    path.pop(0)
    path = sorted(path, key=lambda x:(x[0], x[1]))
    for x, y, n in path:
        answer.append(n)
    return answer
