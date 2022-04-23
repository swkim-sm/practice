import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

move = [(1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)] # h, n, m
cnt = 1

while True:
    # TODO: find tomatoes which are next to ripe tomatoes and change states of them
    change_flag = False
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if tomatoes[z][y][x] == cnt:
                    for i in range(6):
                        nx = x + move[i][2]
                        ny = y + move[i][1]
                        nz = z + move[i][0]
                        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and tomatoes[nz][ny][nx] == 0:
                            tomatoes[nz][ny][nx] = cnt + 1 
                            change_flag = True

    # TODO: break condition : no change (must check if all tomatoes are riped)
    if not change_flag:
        break_flag = False
        for z in range(h):
            for y in range(n):
                for x in range(m):
                    if tomatoes[z][y][x] == 0:
                        print(-1)
                        exit()
        print(cnt-1)
        break
    cnt += 1