import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0]

def solution(m, x, y):
    global ans
    flag = False
    for i in range(x, x+m):
        for j in range(y, y+m):
            if board[i][j] != board[x][y]:
                flag = True
                break
        if flag:
            break
    if flag:
        for i in range(x, x+m, m//2):
            for j in range(y, y+m, m//2):
                solution(m//2, i, j)
    else:
        ans[board[x][y]] += 1

solution(n, 0, 0)


print(ans[0])
print(ans[1])