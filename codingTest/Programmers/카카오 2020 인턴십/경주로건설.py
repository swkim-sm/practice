from collections import deque
def solution(board):
    answer = float('inf')
    n = len(board)
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q = deque()
    q.append((0, 0, -1, 0)) # (x, y, direction, cost)
    # (x, y, direction):cost
    visited = {(0, 0, 0):0, (0, 0, 1):0, (0, 0, 2):0, (0, 0, 3):0}
    while q:
        x, y, pre_d, cost = q.popleft()
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                new_cost = cost
                # 초기값 or 같은 방향
                if pre_d == -1 or (pre_d - d) % 2 == 0:
                    new_cost += 100
                # 다른 방향
                else:
                    new_cost += 600

                # answer update condition
                if nx == n-1 and ny == n-1:
                    answer = min(answer, new_cost)
                # q에 추가하는 조건 : 기존에 방문안했거나 cost가 적은 경우
                elif visited.get((nx, ny, d)) is None or new_cost < visited.get((nx, ny, d)):
                    visited[(nx, ny, d)] = new_cost
                    q.append((nx, ny, d, new_cost))
    return answer
