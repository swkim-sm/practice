import sys
from itertools import combinations, permutations
from collections import deque
from traceback import print_last
Input = sys.stdin.readline

board = []
star_locs = []
for i in range(5):
    tmp = list(Input())
    board.append(tmp)
    for j in range(5):
        if tmp[j] == '*':
            star_locs.append([i, j])
stars = len(star_locs)

def is_connected(locs):
    dq = deque([locs[0]])
    visited = [[False for _ in range(5)] for _ in range(5)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 1
    
    while dq:
        x, y = dq.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if not visited[nx][ny] and [nx, ny] in locs:
                    dq.append([nx, ny])
                    visited[nx][ny] = True
                    cnt += 1
    
    if cnt == len(locs):
        return True
    else:
        return False



# search all of connected cases
answer = sys.maxsize
combi = list(combinations([i for i in range(25)], stars))
for cur_c in combi:
    cur_star_locs = []
    for i in cur_c:
        cur_star_locs.append([i//5, i%5])
    
    if not is_connected(cur_star_locs):
        continue

    # calculate distance from cur case to input case
    perm = list(permutations([i for i in range(stars)], stars))
    for cur_p in perm:
        tmp_distance = 0
        for j in range(stars):
            tmp_distance += (abs(star_locs[j][0]-cur_star_locs[cur_p[j]][0]) + abs(star_locs[j][1]-cur_star_locs[cur_p[j]][1]))
        if tmp_distance < answer:
            answer = tmp_distance


print(answer)