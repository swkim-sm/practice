N, M = map(int, input().split())

A = [[] for _ in range(N)]
for i in range(N):
    A[i] = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def get_max(x, y):
    max_val = 0
    
    arr = [[x, y, A[x][y], 1]] # [x, y, cost, block num]
    visited = [[0 for _ in range(M)] for _ in range(N)]


    while arr:
        cx, cy, val, cnt = arr.pop()
        if visited[cx][cy] < val:
            visited[cx][cy] = val
        else:
            continue

        if cnt == 4:
            max_val = max(max_val, val)
            continue
        
        cnt += 1

        pink = []
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                arr.append([nx, ny, val+A[nx][ny], cnt])
                pink.append(A[nx][ny])

        # if len(pink) == 4 and cnt == 2:
        #     pink.sort(reverse=True)
        #     max_val = max(max_val, A[cx][cy] + sum(pink[:3]))
        #     print(pink, pink[:3], max_val, A[cx][cy] + sum(pink[:3]))
        # elif len(pink) == 3 and cnt == 2:
        #     max_val = max(max_val, A[cx][cy] + sum(pink))
        #     print(pink, max_val, A[cx][cy] + sum(pink))

    return max_val

answer = 0

for i in range(N):
    for j in range(M):
        answer = max(answer, get_max(i, j)) 
        

print(answer)