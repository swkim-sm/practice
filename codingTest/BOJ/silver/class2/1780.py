import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

ans = [0, 0, 0]
def solution(size, x, y):
    global ans
    flag = False
    for i in range(x, x+size):
        for j in range(y, y+size):
            if board[i][j] != board[x][y]:
                flag = True
                break
        if flag:
            break
    if flag:
        for i in range(x, x+size, size//3):
            for j in range(y, y+size, size//3):
                solution(size//3, i, j)
    else:
        ans[board[x][y]+1] += 1
solution(n, 0, 0)
for a in ans:
    print(a)