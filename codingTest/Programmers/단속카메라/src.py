def solution(routes):
    answer = 1
    routes.sort()
    common = [routes[0][0], routes[0][1]]
    
    for route in routes:
        # 범위 겹치는 경우
        if route[0] <= common[1]:
            common[0] = route[0]
            common[1] = min(route[1], common[1])
        else:
            answer += 1
            common = route
            
    return answer
